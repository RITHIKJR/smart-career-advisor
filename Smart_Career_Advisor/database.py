import sqlite3
import hashlib
import json
from datetime import datetime
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name('users.db')

def _connect():
    return sqlite3.connect(DATABASE_PATH, timeout=30)

def init_db():
    conn = _connect()
    conn.execute('PRAGMA journal_mode=WAL')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS assessments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  aptitude_score INTEGER,
                  riasec_type TEXT,
                  recommended_branch TEXT,
                  completed_date TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS learning_paths
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  branch TEXT,
                  modules TEXT,
                  progress TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS study_streak
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  last_study_date TEXT,
                  current_streak INTEGER DEFAULT 0,
                  longest_streak INTEGER DEFAULT 0,
                  total_study_days INTEGER DEFAULT 0,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS goals
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  goal_text TEXT,
                  target_date TEXT,
                  completed INTEGER DEFAULT 0,
                  created_date TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  module_name TEXT,
                  note_text TEXT,
                  created_date TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS saved_scholarships
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  scholarship_id INTEGER,
                  saved_date TEXT,
                  applied INTEGER DEFAULT 0,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS external_courses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  module_name TEXT,
                  platform TEXT,
                  course_name TEXT,
                  url TEXT,
                  started_date TEXT,
                  completed INTEGER DEFAULT 0,
                  completion_date TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    conn = _connect()
    try:
        with conn:
            conn.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hash_password(password)),
            )
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(email, password):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?",
              (email, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

def get_user_id(username):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user[0] if user else None

def save_assessment(user_id, aptitude_score, riasec_type, recommended_branch):
    conn = _connect()
    c = conn.cursor()
    c.execute("INSERT INTO assessments (user_id, aptitude_score, riasec_type, recommended_branch, completed_date) VALUES (?, ?, ?, ?, ?)",
              (user_id, aptitude_score, riasec_type, recommended_branch, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

def get_assessment(user_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM assessments WHERE user_id=? ORDER BY id DESC LIMIT 1", (user_id,))
    result = c.fetchone()
    conn.close()
    return result

def save_learning_path(user_id, branch, modules, progress):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT id FROM learning_paths WHERE user_id=?", (user_id,))
    existing = c.fetchone()
    
    if existing:
        c.execute("UPDATE learning_paths SET branch=?, modules=?, progress=? WHERE user_id=?",
                  (branch, json.dumps(modules), json.dumps(progress), user_id))
    else:
        c.execute("INSERT INTO learning_paths (user_id, branch, modules, progress) VALUES (?, ?, ?, ?)",
                  (user_id, branch, json.dumps(modules), json.dumps(progress)))
    conn.commit()
    conn.close()

def get_learning_path(user_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM learning_paths WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result

def update_study_streak(user_id):
    conn = _connect()
    c = conn.cursor()
    today = datetime.now().strftime('%Y-%m-%d')
    
    c.execute("SELECT * FROM study_streak WHERE user_id=?", (user_id,))
    streak = c.fetchone()
    
    if not streak:
        c.execute("INSERT INTO study_streak (user_id, last_study_date, current_streak, longest_streak, total_study_days) VALUES (?, ?, 1, 1, 1)",
                  (user_id, today))
    else:
        last_date = datetime.strptime(streak[2], '%Y-%m-%d')
        today_date = datetime.strptime(today, '%Y-%m-%d')
        diff = (today_date - last_date).days
        
        if diff == 0:
            pass
        elif diff == 1:
            new_streak = streak[3] + 1
            new_longest = max(new_streak, streak[4])
            c.execute("UPDATE study_streak SET last_study_date=?, current_streak=?, longest_streak=?, total_study_days=? WHERE user_id=?",
                      (today, new_streak, new_longest, streak[5] + 1, user_id))
        else:
            c.execute("UPDATE study_streak SET last_study_date=?, current_streak=1, total_study_days=? WHERE user_id=?",
                      (today, streak[5] + 1, user_id))
    
    conn.commit()
    conn.close()

def get_study_streak(user_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM study_streak WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result

def add_goal(user_id, goal_text, target_date):
    conn = _connect()
    c = conn.cursor()
    c.execute("INSERT INTO goals (user_id, goal_text, target_date, created_date) VALUES (?, ?, ?, ?)",
              (user_id, goal_text, target_date, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

def get_goals(user_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM goals WHERE user_id=? ORDER BY completed ASC, target_date ASC", (user_id,))
    results = c.fetchall()
    conn.close()
    return results

def toggle_goal(goal_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("UPDATE goals SET completed = 1 - completed WHERE id=?", (goal_id,))
    conn.commit()
    conn.close()

def add_note(user_id, module_name, note_text):
    conn = _connect()
    c = conn.cursor()
    c.execute("INSERT INTO notes (user_id, module_name, note_text, created_date) VALUES (?, ?, ?, ?)",
              (user_id, module_name, note_text, datetime.now().strftime('%Y-%m-%d %H:%M')))
    conn.commit()
    conn.close()

def get_notes(user_id, module_name=None):
    conn = _connect()
    c = conn.cursor()
    if module_name:
        c.execute("SELECT * FROM notes WHERE user_id=? AND module_name=? ORDER BY id DESC", (user_id, module_name))
    else:
        c.execute("SELECT * FROM notes WHERE user_id=? ORDER BY id DESC", (user_id,))
    results = c.fetchall()
    conn.close()
    return results

def save_scholarship(user_id, scholarship_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM saved_scholarships WHERE user_id=? AND scholarship_id=?", (user_id, scholarship_id))
    if not c.fetchone():
        c.execute("INSERT INTO saved_scholarships (user_id, scholarship_id, saved_date) VALUES (?, ?, ?)",
                  (user_id, scholarship_id, datetime.now().strftime('%Y-%m-%d')))
        conn.commit()
    conn.close()

def get_saved_scholarships(user_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM saved_scholarships WHERE user_id=?", (user_id,))
    results = c.fetchall()
    conn.close()
    return results

def toggle_scholarship_applied(user_id, scholarship_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("UPDATE saved_scholarships SET applied = 1 - applied WHERE user_id=? AND scholarship_id=?",
              (user_id, scholarship_id))
    conn.commit()
    conn.close()

def start_external_course(user_id, module_name, platform, course_name, url):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT * FROM external_courses WHERE user_id=? AND url=?", (user_id, url))
    if not c.fetchone():
        c.execute("INSERT INTO external_courses (user_id, module_name, platform, course_name, url, started_date) VALUES (?, ?, ?, ?, ?, ?)",
                  (user_id, module_name, platform, course_name, url, datetime.now().strftime('%Y-%m-%d')))
        conn.commit()
    conn.close()

def complete_external_course(user_id, course_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("UPDATE external_courses SET completed=1, completion_date=? WHERE id=? AND user_id=?",
              (datetime.now().strftime('%Y-%m-%d'), course_id, user_id))
    conn.commit()
    conn.close()

def get_external_courses(user_id, module_name=None):
    conn = _connect()
    c = conn.cursor()
    if module_name:
        c.execute("SELECT * FROM external_courses WHERE user_id=? AND module_name=? ORDER BY started_date DESC", (user_id, module_name))
    else:
        c.execute("SELECT * FROM external_courses WHERE user_id=? ORDER BY started_date DESC", (user_id,))
    results = c.fetchall()
    conn.close()
    return results
