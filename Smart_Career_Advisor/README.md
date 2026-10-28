# 🎓 Smart Career Advisor

AI-powered career guidance platform with ML-based college recommendations, personality assessments, and personalized learning paths.

## ✨ Features

- 📊 **Smart Assessments** - Aptitude & RIASEC personality tests
- 🎯 **Career Matching** - ML-powered college recommendations
- 📚 **Learning Paths** - Structured course modules
- 💰 **Scholarship Finder** - 18+ real scholarships
- 🏫 **College Finder** - Location, type, and placement data
- 🔥 **Gamification** - Streaks, goals, achievements
- 📝 **Study Notes** - Organized note-taking system

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Extract the project** (if ZIP file)
   ```bash
   unzip Smart_Career_Advisor.zip
   cd Smart_Career_Advisor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python server.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
Smart_Career_Advisor/
├── server.py                 # Flask backend
├── database.py              # SQLite database functions
├── assessment_data.py       # Assessment questions & data
├── scholarship_data.py      # Scholarship database
├── placement_data.py        # Placement statistics
├── college_type_data.py     # College classification
├── college_location_data.py # College locations
├── college_model.pkl        # ML model
├── tnea_cutoff_clean.csv   # College cutoff data
├── users.db                 # SQLite database (auto-created)
├── requirements.txt         # Python dependencies
├── templates/               # HTML templates
│   ├── home.html
│   ├── index.html
│   ├── aptitude.html
│   └── riasec.html
└── static/                  # CSS & JavaScript
    ├── style.css
    ├── landing.css
    ├── script.js
    └── assessment.js
```

## 🎮 How to Use

1. **Home Page** - Visit http://localhost:5000
2. **Register** - Create a new account
3. **Take Assessment** - Complete aptitude & RIASEC tests
4. **View Results** - See recommended course & placement stats
5. **Find Colleges** - Get ML-powered college recommendations
6. **Explore Features** - Goals, notes, scholarships, learning paths

## 🔧 Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **ML Model**: Scikit-learn
- **Frontend**: HTML, CSS, JavaScript
- **Data**: Pandas, NumPy

## 📊 Database Tables

- `users` - User accounts
- `assessments` - Test results
- `learning_paths` - Progress tracking
- `study_streak` - Gamification data
- `goals` - Goal tracking
- `notes` - Study notes
- `saved_scholarships` - Saved scholarships

## 🎯 Key Features Explained

### ML-Powered Recommendations
- Uses trained model (college_model.pkl)
- Predicts admission probability based on cutoff scores
- Realistic probability scaling (75-95% range)

### RIASEC Assessment
- Maps personality types to engineering branches:
  - R → Mechanical Engineering
  - I → Computer Science
  - A → Computer Science & Design
  - S → Bio Medical Engineering
  - E → Industrial Engineering
  - C → Civil Engineering

### Real Data
- 18 verified scholarships (Government/State/Private)
- Placement statistics from AICTE reports
- 25+ colleges with GPS coordinates
- College type classification (Government/Aided/Self-Financing)

## 🐛 Troubleshooting

**Port already in use:**
```bash
python server.py --port 5001
```

**Missing dependencies:**
```bash
pip install flask pandas scikit-learn
```

**Database errors:**
Delete `users.db` and restart - it will auto-recreate

## 📝 Notes

- First-time setup creates `users.db` automatically
- ML model is pre-trained (college_model.pkl)
- Sample data included for testing
- All scholarships are real and verified

## 👥 Credits

Developed as a career guidance platform for engineering students in Tamil Nadu.

## 📧 Support

For issues or questions, contact the developer.

---

**Enjoy using Smart Career Advisor! 🚀**
