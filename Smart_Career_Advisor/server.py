from flask import Flask, render_template, request, jsonify, session
from database import init_db, register_user, login_user, get_user_id, save_assessment, get_assessment, save_learning_path, get_learning_path, update_study_streak, get_study_streak, add_goal, get_goals, toggle_goal, add_note, get_notes, save_scholarship, get_saved_scholarships, toggle_scholarship_applied, start_external_course, complete_external_course, get_external_courses
from assessment_data import APTITUDE_QUESTIONS, RIASEC_QUESTIONS, RIASEC_TO_BRANCH, LEARNING_PATHS
from scholarship_data import SCHOLARSHIPS, SUCCESS_STORIES
from placement_data import get_placement_stats, get_career_insights
from college_type_data import get_college_type
from college_location_data import get_college_location, get_google_maps_url, get_distance_category
import pandas as pd
import pickle
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

init_db()

model = pickle.load(open("college_model.pkl", "rb"))
data = pd.read_csv("tnea_cutoff_clean.csv")
data.columns = data.columns.str.strip()

long_data = data.melt(
    id_vars=["college_code", "college", "branch"],
    value_vars=["OC", "BC", "BCM", "MBC", "SC", "SCA", "ST"],
    var_name="Category",
    value_name="Required_Cutoff"
).dropna()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/aptitude')
def aptitude():
    return render_template('aptitude.html')

@app.route('/riasec')
def riasec():
    return render_template('riasec.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    if register_user(data['username'], data['email'], data['password']):
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'User already exists'})

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    user = login_user(data['email'], data['password'])
    if user:
        session['email'] = data['email']
        session['username'] = user[1]  # username from database
        session['user_id'] = user[0]
        return jsonify({'success': True, 'username': user[1]})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.pop('email', None)
    session.pop('username', None)
    session.pop('user_id', None)
    return jsonify({'success': True})

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})
    
    data = request.json
    cutoff = float(data['cutoff'])
    category = data['category']
    branch = data['branch']  # This comes from RIASEC assessment result
    
    branch_map = {
        "Computer Science and Engineering": ["COMPUTER SCIENCE", "CSE", "CS", "INFORMATION TECHNOLOGY", "IT", "ARTIFICIAL INTELLIGENCE", "AI", "DATA SCIENCE", "MACHINE LEARNING"],
        "Mechanical Engineering": ["MECHANICAL", "MECH", "AUTOMOBILE", "AUTO", "PRODUCTION", "MANUFACTURING", "AERONAUTICAL", "AEROSPACE"],
        "Civil Engineering": ["CIVIL", "CONSTRUCTION", "STRUCTURAL"],
        "Bio Medical Engineering": ["BIO MEDICAL", "BIOMEDICAL", "BME", "BIOTECHNOLOGY", "BIO TECH"],
        "Industrial Engineering": ["INDUSTRIAL", "PRODUCTION", "MANUFACTURING"],
        "Computer Science and Design": ["COMPUTER SCIENCE AND DESIGN", "CSD", "COMPUTER SCIENCE", "CSE"],
        "Electronics and Communication Engineering": ["ELECTRONICS AND COMMUNICATION", "ECE", "ELECTRONICS", "COMMUNICATION"],
        "Electrical and Electronics Engineering": ["ELECTRICAL AND ELECTRONICS", "EEE", "ELECTRICAL"],
        "Information Technology": ["INFORMATION TECHNOLOGY", "IT", "COMPUTER SCIENCE", "CSE"]
    }
    branch_keywords = branch_map.get(branch, [branch.upper()])
    
    recommendations = []
    for _, row in long_data.iterrows():
        if category != row["Category"]:
            continue
        
        branch_str = str(row["branch"]).upper()
        if not any(keyword in branch_str for keyword in branch_keywords):
            continue
        
        required_cutoff = row["Required_Cutoff"]
        cutoff_diff = cutoff - required_cutoff
        
        # Filter: Only show colleges within reasonable range
        # Show colleges where student cutoff is -10 to +30 of required cutoff
        if cutoff_diff < -10 or cutoff_diff > 30:
            continue
        
        input_dict = {"Student_Cutoff": cutoff, "Required_Cutoff": required_cutoff}
        for col in model.feature_names_in_:
            if col.startswith("Category_"):
                input_dict[col] = 1 if col == f"Category_{category}" else 0
        
        input_df = pd.DataFrame([input_dict])
        probability = model.predict_proba(input_df)[0][1]
        
        # Apply realistic probability scaling
        if cutoff_diff >= 15:
            probability = min(probability, 0.95)
        elif cutoff_diff >= 10:
            probability = min(probability, 0.90)
        elif cutoff_diff >= 5:
            probability = min(probability, 0.85)
        elif cutoff_diff >= 0:
            probability = min(probability, 0.75)
        
        recommendations.append({
            'code': row["college_code"],
            'name': row["college"],
            'branch': row["branch"],
            'cutoff': required_cutoff,
            'probability': round(probability * 100, 2),
            'college_type': get_college_type(row["college"]),
            'location': get_college_location(row["college_code"]),
            'maps_url': get_google_maps_url(row["college_code"], row["college"])
        })
    
    recommendations.sort(reverse=True, key=lambda x: x['probability'])
    return jsonify({'success': True, 'data': recommendations[:10]})

@app.route('/api/aptitude-questions', methods=['GET'])
def get_aptitude():
    return jsonify({'questions': APTITUDE_QUESTIONS})

@app.route('/api/riasec-questions', methods=['GET'])
def get_riasec():
    return jsonify({'questions': RIASEC_QUESTIONS})

@app.route('/api/submit-assessment', methods=['POST'])
def submit_assessment():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})
    
    data = request.json
    aptitude_score = data['aptitude_score']
    riasec_scores = data['riasec_scores']
    
    top_type = max(riasec_scores, key=riasec_scores.get)
    recommended = RIASEC_TO_BRANCH[top_type]
    
    save_assessment(session['user_id'], aptitude_score, top_type, recommended['branch'])
    
    return jsonify({
        'success': True,
        'riasec_type': top_type,
        'recommended_branch': recommended['branch'],
        'description': recommended['desc'],
        'aptitude_score': aptitude_score
    })

@app.route('/api/get-assessment', methods=['GET'])
def get_user_assessment():
    if 'user_id' not in session:
        return jsonify({'success': False})
    
    result = get_assessment(session['user_id'])
    if result:
        return jsonify({
            'success': True,
            'aptitude_score': result[2],
            'riasec_type': result[3],
            'recommended_branch': result[4],
            'completed_date': result[5]
        })
    return jsonify({'success': False})

@app.route('/api/learning-path/<branch>', methods=['GET'])
def get_branch_learning_path(branch):
    path = LEARNING_PATHS.get(branch, [])
    return jsonify({'success': True, 'modules': path})

@app.route('/api/save-progress', methods=['POST'])
def save_progress():
    if 'user_id' not in session:
        return jsonify({'success': False})
    
    data = request.json
    save_learning_path(session['user_id'], data['branch'], data['modules'], data['progress'])
    return jsonify({'success': True})

@app.route('/api/get-progress', methods=['GET'])
def get_progress():
    if 'user_id' not in session:
        return jsonify({'success': False})
    
    result = get_learning_path(session['user_id'])
    if result:
        return jsonify({
            'success': True,
            'branch': result[2],
            'modules': json.loads(result[3]),
            'progress': json.loads(result[4])
        })
    return jsonify({'success': False})

@app.route('/api/study-streak', methods=['POST'])
def update_streak():
    if 'user_id' not in session:
        return jsonify({'success': False})
    update_study_streak(session['user_id'])
    return jsonify({'success': True})

@app.route('/api/get-streak', methods=['GET'])
def get_streak():
    if 'user_id' not in session:
        return jsonify({'success': False})
    streak = get_study_streak(session['user_id'])
    if streak:
        return jsonify({
            'success': True,
            'current_streak': streak[3],
            'longest_streak': streak[4],
            'total_days': streak[5]
        })
    return jsonify({'success': True, 'current_streak': 0, 'longest_streak': 0, 'total_days': 0})

@app.route('/api/goals', methods=['GET'])
def get_user_goals():
    if 'user_id' not in session:
        return jsonify({'success': False})
    goals = get_goals(session['user_id'])
    return jsonify({
        'success': True,
        'goals': [{'id': g[0], 'text': g[2], 'target': g[3], 'completed': g[4], 'created': g[5]} for g in goals]
    })

@app.route('/api/goals', methods=['POST'])
def create_goal():
    if 'user_id' not in session:
        return jsonify({'success': False})
    data = request.json
    add_goal(session['user_id'], data['goal_text'], data['target_date'])
    return jsonify({'success': True})

@app.route('/api/goals/<int:goal_id>/toggle', methods=['POST'])
def toggle_goal_status(goal_id):
    if 'user_id' not in session:
        return jsonify({'success': False})
    toggle_goal(goal_id)
    return jsonify({'success': True})

@app.route('/api/notes', methods=['GET'])
def get_user_notes():
    if 'user_id' not in session:
        return jsonify({'success': False})
    module = request.args.get('module')
    notes = get_notes(session['user_id'], module)
    return jsonify({
        'success': True,
        'notes': [{'id': n[0], 'module': n[2], 'text': n[3], 'date': n[4]} for n in notes]
    })

@app.route('/api/notes', methods=['POST'])
def create_note():
    if 'user_id' not in session:
        return jsonify({'success': False})
    data = request.json
    add_note(session['user_id'], data['module_name'], data['note_text'])
    return jsonify({'success': True})

@app.route('/api/dashboard-stats', methods=['GET'])
def dashboard_stats():
    if 'user_id' not in session:
        return jsonify({'success': False})
    
    assessment = get_assessment(session['user_id'])
    learning = get_learning_path(session['user_id'])
    streak = get_study_streak(session['user_id'])
    goals = get_goals(session['user_id'])
    
    total_modules = 0
    completed_modules = 0
    if learning:
        progress = json.loads(learning[4])
        total_modules = len(progress)
        completed_modules = sum(1 for p in progress.values() if p == 100)
    
    completed_goals = sum(1 for g in goals if g[4] == 1)
    
    return jsonify({
        'success': True,
        'assessment_completed': assessment is not None,
        'total_modules': total_modules,
        'completed_modules': completed_modules,
        'current_streak': streak[3] if streak else 0,
        'total_goals': len(goals),
        'completed_goals': completed_goals
    })

@app.route('/api/scholarships', methods=['GET'])
def get_scholarships():
    category = request.args.get('category', 'All')
    scholarship_type = request.args.get('type', 'All')
    first_grad = request.args.get('first_graduate', 'false').lower() == 'true'
    
    filtered = SCHOLARSHIPS
    
    if category != 'All':
        filtered = [s for s in filtered if category in s['eligibility']['category'] or 'All' in s['eligibility']['category']]
    
    if scholarship_type != 'All':
        filtered = [s for s in filtered if s['type'] == scholarship_type]
    
    if first_grad:
        filtered = [s for s in filtered if s['first_graduate']]
    
    return jsonify({'success': True, 'scholarships': filtered})

@app.route('/api/scholarships/<int:scholarship_id>', methods=['GET'])
def get_scholarship_detail(scholarship_id):
    scholarship = next((s for s in SCHOLARSHIPS if s['id'] == scholarship_id), None)
    if scholarship:
        return jsonify({'success': True, 'scholarship': scholarship})
    return jsonify({'success': False, 'message': 'Scholarship not found'})

@app.route('/api/scholarships/save', methods=['POST'])
def save_user_scholarship():
    if 'user_id' not in session:
        return jsonify({'success': False})
    data = request.json
    save_scholarship(session['user_id'], data['scholarship_id'])
    return jsonify({'success': True})

@app.route('/api/scholarships/saved', methods=['GET'])
def get_user_saved_scholarships():
    if 'user_id' not in session:
        return jsonify({'success': False})
    saved = get_saved_scholarships(session['user_id'])
    saved_ids = [s[2] for s in saved]
    saved_scholarships = [s for s in SCHOLARSHIPS if s['id'] in saved_ids]
    applied_ids = [s[2] for s in saved if s[4] == 1]
    return jsonify({
        'success': True,
        'scholarships': saved_scholarships,
        'applied_ids': applied_ids
    })

@app.route('/api/scholarships/toggle-applied', methods=['POST'])
def toggle_applied():
    if 'user_id' not in session:
        return jsonify({'success': False})
    data = request.json
    toggle_scholarship_applied(session['user_id'], data['scholarship_id'])
    return jsonify({'success': True})

@app.route('/api/scholarships/success-stories', methods=['GET'])
def get_success_stories():
    return jsonify({'success': True, 'stories': SUCCESS_STORIES})

@app.route('/api/placement-stats/<branch>', methods=['GET'])
def get_branch_placement_stats(branch):
    stats = get_placement_stats(branch)
    insights = get_career_insights(branch)
    if stats:
        return jsonify({
            'success': True,
            'placement': stats,
            'insights': insights
        })
    return jsonify({'success': False, 'message': 'Branch not found'})

@app.route('/api/check-session', methods=['GET'])
def check_session():
    return jsonify({'logged_in': 'user_id' in session})

@app.route('/api/external-courses/start', methods=['POST'])
def start_course():
    if 'user_id' not in session:
        return jsonify({'success': False})
    data = request.json
    start_external_course(session['user_id'], data['module_name'], data['platform'], data['course_name'], data['url'])
    return jsonify({'success': True})

@app.route('/api/external-courses/complete', methods=['POST'])
def complete_course():
    if 'user_id' not in session:
        return jsonify({'success': False})
    data = request.json
    complete_external_course(session['user_id'], data['course_id'])
    return jsonify({'success': True})

@app.route('/api/external-courses', methods=['GET'])
def get_user_courses():
    if 'user_id' not in session:
        return jsonify({'success': False})
    module = request.args.get('module')
    courses = get_external_courses(session['user_id'], module)
    return jsonify({
        'success': True,
        'courses': [{'id': c[0], 'module': c[2], 'platform': c[3], 'name': c[4], 'url': c[5], 'started': c[6], 'completed': c[7], 'completion_date': c[8]} for c in courses]
    })



if __name__ == '__main__':
    app.run(debug=True, port=5000)
