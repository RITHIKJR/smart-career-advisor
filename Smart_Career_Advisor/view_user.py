import sqlite3

def view_user_data(email):
    """View all data for a specific user"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Get user info
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    
    if not user:
        print(f"❌ User with email '{email}' not found!")
        conn.close()
        return
    
    user_id = user[0]
    username = user[1]
    
    print("=" * 80)
    print(f"👤 USER PROFILE: {username}")
    print("=" * 80)
    print(f"Email: {email}")
    print(f"User ID: {user_id}")
    
    # Assessment data
    print("\n📊 ASSESSMENT RESULTS:")
    cursor.execute("SELECT * FROM assessments WHERE user_id=?", (user_id,))
    assessment = cursor.fetchone()
    if assessment:
        print(f"   Aptitude Score: {assessment[2]}/10")
        print(f"   RIASEC Type: {assessment[3]}")
        print(f"   Recommended Branch: {assessment[4]}")
        print(f"   Completed Date: {assessment[5]}")
    else:
        print("   No assessment completed yet")
    
    # Goals
    print("\n🎯 GOALS:")
    cursor.execute("SELECT * FROM goals WHERE user_id=?", (user_id,))
    goals = cursor.fetchall()
    if goals:
        for goal in goals:
            status = "✅" if goal[4] == 1 else "⏳"
            print(f"   {status} {goal[2]} (Target: {goal[3]})")
    else:
        print("   No goals set yet")
    
    # Notes
    print("\n📝 NOTES:")
    cursor.execute("SELECT * FROM notes WHERE user_id=?", (user_id,))
    notes = cursor.fetchall()
    if notes:
        print(f"   Total Notes: {len(notes)}")
        for note in notes[:3]:  # Show first 3
            print(f"   - {note[2]}: {note[3][:50]}...")
    else:
        print("   No notes yet")
    
    # Streak
    print("\n🔥 STUDY STREAK:")
    cursor.execute("SELECT * FROM study_streak WHERE user_id=?", (user_id,))
    streak = cursor.fetchone()
    if streak:
        print(f"   Current Streak: {streak[3]} days")
        print(f"   Longest Streak: {streak[4]} days")
        print(f"   Total Study Days: {streak[5]} days")
    else:
        print("   No streak data yet")
    
    # Saved Scholarships
    print("\n💰 SAVED SCHOLARSHIPS:")
    cursor.execute("SELECT * FROM saved_scholarships WHERE user_id=?", (user_id,))
    scholarships = cursor.fetchall()
    if scholarships:
        print(f"   Total Saved: {len(scholarships)}")
        applied = sum(1 for s in scholarships if s[4] == 1)
        print(f"   Applied: {applied}")
    else:
        print("   No scholarships saved yet")
    
    conn.close()
    print("\n" + "=" * 80)

if __name__ == "__main__":
    email = input("Enter user email: ")
    view_user_data(email)
