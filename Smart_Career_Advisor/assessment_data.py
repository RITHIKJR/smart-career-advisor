APTITUDE_QUESTIONS = [
    {"q": "If a train travels 120 km in 2 hours, what is its speed?", "options": ["50 km/h", "60 km/h", "70 km/h", "80 km/h"], "answer": 1},
    {"q": "Complete the series: 2, 6, 12, 20, ?", "options": ["28", "30", "32", "34"], "answer": 1},
    {"q": "If 5x + 3 = 18, what is x?", "options": ["2", "3", "4", "5"], "answer": 1},
    {"q": "What is 15% of 200?", "options": ["25", "30", "35", "40"], "answer": 1},
    {"q": "A cube has how many edges?", "options": ["6", "8", "10", "12"], "answer": 3},
    {"q": "If A=1, B=2, C=3, what is CAB?", "options": ["312", "321", "123", "213"], "answer": 0},
    {"q": "What comes next: 1, 4, 9, 16, ?", "options": ["20", "25", "30", "36"], "answer": 1},
    {"q": "If today is Monday, what day is 100 days from now?", "options": ["Monday", "Tuesday", "Wednesday", "Thursday"], "answer": 1},
    {"q": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "answer": 2},
    {"q": "If 3 workers complete a task in 6 days, how many days for 6 workers?", "options": ["2", "3", "4", "5"], "answer": 1}
]

RIASEC_QUESTIONS = [
    {"q": "I enjoy working with tools and machines", "type": "R"},
    {"q": "I like solving complex problems and puzzles", "type": "I"},
    {"q": "I enjoy creating art, music, or writing", "type": "A"},
    {"q": "I like helping and teaching others", "type": "S"},
    {"q": "I enjoy leading teams and making decisions", "type": "E"},
    {"q": "I prefer organized and structured tasks", "type": "C"},
    {"q": "I like outdoor activities and physical work", "type": "R"},
    {"q": "I enjoy conducting experiments and research", "type": "I"},
    {"q": "I like designing and creating new things", "type": "A"},
    {"q": "I enjoy counseling and supporting people", "type": "S"},
    {"q": "I like persuading and influencing others", "type": "E"},
    {"q": "I prefer working with data and details", "type": "C"},
    {"q": "I enjoy building and repairing things", "type": "R"},
    {"q": "I like analyzing data and finding patterns", "type": "I"},
    {"q": "I enjoy performing and expressing creativity", "type": "A"},
    {"q": "I like working in healthcare or social services", "type": "S"},
    {"q": "I enjoy managing projects and resources", "type": "E"},
    {"q": "I prefer following procedures and rules", "type": "C"}
]

RIASEC_TO_BRANCH = {
    "R": {"branch": "Mechanical Engineering", "desc": "Hands-on work with machines and tools"},
    "I": {"branch": "Computer Science and Engineering", "desc": "Problem-solving and analytical thinking"},
    "A": {"branch": "Computer Science and Design", "desc": "Creative and innovative design work"},
    "S": {"branch": "Bio Medical Engineering", "desc": "Helping people through technology"},
    "E": {"branch": "Industrial Engineering", "desc": "Management and optimization"},
    "C": {"branch": "Civil Engineering", "desc": "Structured planning and execution"}
}

LEARNING_PATHS = {
    "Computer Science and Engineering": [
        {"module": "Programming Fundamentals", "topics": ["Python", "Java", "C++"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Python for Everybody", "url": "https://www.coursera.org/specializations/python", "free": True},
            {"platform": "YouTube", "name": "FreeCodeCamp Python", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "free": True},
            {"platform": "Udemy", "name": "Complete Python Bootcamp", "url": "https://www.udemy.com/course/complete-python-bootcamp/", "free": False}
        ]},
        {"module": "Data Structures & Algorithms", "topics": ["Arrays", "Trees", "Graphs"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "Data Structures by UC San Diego", "url": "https://www.coursera.org/learn/data-structures", "free": True},
            {"platform": "YouTube", "name": "Abdul Bari DSA", "url": "https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O", "free": True}
        ]},
        {"module": "Database Management", "topics": ["SQL", "NoSQL", "MongoDB"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "SQL for Data Science", "url": "https://www.coursera.org/learn/sql-for-data-science", "free": True},
            {"platform": "YouTube", "name": "MongoDB Crash Course", "url": "https://www.youtube.com/watch?v=ofme2o29ngU", "free": True}
        ]},
        {"module": "Web Development", "topics": ["HTML/CSS", "JavaScript", "React"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Web Design for Everybody", "url": "https://www.coursera.org/specializations/web-design", "free": True},
            {"platform": "YouTube", "name": "Traversy Media Web Dev", "url": "https://www.youtube.com/c/TraversyMedia", "free": True}
        ]},
        {"module": "Machine Learning", "topics": ["ML Basics", "Deep Learning", "AI"], "duration": "4 months", "courses": [
            {"platform": "Coursera", "name": "Machine Learning by Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning", "free": True},
            {"platform": "YouTube", "name": "Sentdex ML Tutorial", "url": "https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v", "free": True}
        ]}
    ],
    "Mechanical Engineering": [
        {"module": "Engineering Mechanics", "topics": ["Statics", "Dynamics", "Kinematics"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Engineering Mechanics", "url": "https://www.coursera.org/learn/engineering-mechanics-statics", "free": True},
            {"platform": "YouTube", "name": "Engineering Mechanics Lectures", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngcdUbBySzyzcARZZlskZXJQ", "free": True}
        ]},
        {"module": "Thermodynamics", "topics": ["Heat Transfer", "Energy Systems"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Thermodynamics Course", "url": "https://www.youtube.com/playlist?list=PLZOZfX_TaWAGocs2k5QmTL44OKOl7rn34", "free": True}
        ]},
        {"module": "CAD/CAM", "topics": ["AutoCAD", "SolidWorks", "3D Modeling"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "AutoCAD Complete Tutorial", "url": "https://www.youtube.com/watch?v=JTB_0Xeqy8k", "free": True},
            {"platform": "Udemy", "name": "SolidWorks Masterclass", "url": "https://www.udemy.com/course/solidworks-tutorial/", "free": False}
        ]},
        {"module": "Manufacturing", "topics": ["Machining", "Welding", "CNC"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Manufacturing Processes", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Robotics", "topics": ["Automation", "Control Systems"], "duration": "4 months", "courses": [
            {"platform": "Coursera", "name": "Robotics Specialization", "url": "https://www.coursera.org/specializations/robotics", "free": True}
        ]}
    ],
    "Civil Engineering": [
        {"module": "Structural Analysis", "topics": ["Beams", "Columns", "Frames"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Structural Analysis Lectures", "url": "https://www.youtube.com/playlist?list=PLOAuB8dR35oc8Y5NKZC8JA0v0bK8FhILT", "free": True}
        ]},
        {"module": "Construction Materials", "topics": ["Concrete", "Steel", "Composites"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Construction Materials Course", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Surveying", "topics": ["Land Survey", "GPS", "GIS"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Surveying Complete Course", "url": "https://www.youtube.com/playlist?list=PLOAuB8dR35ocYJz5m0ZZGM7RhXHvQBOZO", "free": True}
        ]},
        {"module": "Transportation", "topics": ["Highway", "Traffic", "Urban Planning"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Transportation Engineering", "url": "https://www.coursera.org/learn/transportation-engineering", "free": True}
        ]},
        {"module": "Environmental Engineering", "topics": ["Water", "Waste Management"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Environmental Engineering", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]}
    ],
    "Bio Medical Engineering": [
        {"module": "Human Anatomy & Physiology", "topics": ["Body Systems", "Organs", "Tissues"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Anatomy Specialization", "url": "https://www.coursera.org/specializations/anatomy", "free": True},
            {"platform": "YouTube", "name": "Crash Course Anatomy", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtOAKed_MxxWBNaPno5h3Zs8", "free": True}
        ]},
        {"module": "Medical Instrumentation", "topics": ["ECG", "MRI", "Ultrasound"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Medical Instrumentation", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Biomaterials", "topics": ["Implants", "Prosthetics", "Tissue Engineering"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "Biomaterials Science", "url": "https://www.coursera.org/learn/biomaterials", "free": True}
        ]},
        {"module": "Medical Imaging", "topics": ["X-Ray", "CT Scan", "Image Processing"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Medical Imaging Course", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Rehabilitation Engineering", "topics": ["Assistive Devices", "Mobility Aids"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Rehabilitation Engineering", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]}
    ],
    "Industrial Engineering": [
        {"module": "Operations Research", "topics": ["Linear Programming", "Optimization", "Simulation"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Operations Research", "url": "https://www.coursera.org/learn/operations-research-modeling", "free": True},
            {"platform": "YouTube", "name": "Operations Research Lectures", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Supply Chain Management", "topics": ["Logistics", "Inventory", "Distribution"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "Supply Chain Management", "url": "https://www.coursera.org/specializations/supply-chain-management", "free": True}
        ]},
        {"module": "Quality Control", "topics": ["Six Sigma", "TQM", "Statistical Process Control"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Six Sigma Training", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Production Planning", "topics": ["Scheduling", "Capacity Planning", "Lean Manufacturing"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Lean Manufacturing Course", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]},
        {"module": "Ergonomics", "topics": ["Workplace Design", "Human Factors", "Safety"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Ergonomics Fundamentals", "url": "https://www.youtube.com/playlist?list=PLbRMhDVUMngfhKwJ7EpBdGCGmCCUF_Uw8", "free": True}
        ]}
    ],
    "Computer Science and Design": [
        {"module": "UI/UX Design Fundamentals", "topics": ["Design Thinking", "User Research", "Wireframing"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "UI/UX Design Specialization", "url": "https://www.coursera.org/specializations/ui-ux-design", "free": True},
            {"platform": "YouTube", "name": "UX Design Course", "url": "https://www.youtube.com/watch?v=c9Wg6Cb_YlU", "free": True}
        ]},
        {"module": "Web Design", "topics": ["HTML/CSS", "Responsive Design", "Figma"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Figma Tutorial", "url": "https://www.youtube.com/watch?v=FTFaQWZBqQ8", "free": True},
            {"platform": "Udemy", "name": "Complete Web Design", "url": "https://www.udemy.com/course/web-design-secrets/", "free": False}
        ]},
        {"module": "Interaction Design", "topics": ["Prototyping", "Animation", "Micro-interactions"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Interaction Design", "url": "https://www.coursera.org/specializations/interaction-design", "free": True}
        ]},
        {"module": "Visual Design", "topics": ["Typography", "Color Theory", "Layout"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Graphic Design Masterclass", "url": "https://www.youtube.com/watch?v=9QTCvayLhCA", "free": True}
        ]},
        {"module": "Frontend Development", "topics": ["JavaScript", "React", "CSS Frameworks"], "duration": "4 months", "courses": [
            {"platform": "Coursera", "name": "React Specialization", "url": "https://www.coursera.org/specializations/react", "free": True},
            {"platform": "YouTube", "name": "React Full Course", "url": "https://www.youtube.com/watch?v=bMknfKXIFA8", "free": True}
        ]}
    ],
    "Electronics and Communication Engineering": [
        {"module": "Circuit Theory", "topics": ["AC/DC Circuits", "Network Analysis", "Filters"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Circuit Theory Lectures", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRhG6s3jYIU48CqsT5cyiDTO", "free": True},
            {"platform": "Coursera", "name": "Circuit Analysis", "url": "https://www.coursera.org/learn/circuit-analysis", "free": True}
        ]},
        {"module": "Digital Electronics", "topics": ["Logic Gates", "Flip-Flops", "Microprocessors"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Digital Electronics Course", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm", "free": True}
        ]},
        {"module": "Communication Systems", "topics": ["Analog Communication", "Digital Communication", "Wireless"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Communication Systems", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgglCEV6WDVT0RjkLRxvYJc", "free": True}
        ]},
        {"module": "Signal Processing", "topics": ["DSP", "Filters", "FFT"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "Digital Signal Processing", "url": "https://www.coursera.org/learn/dsp", "free": True}
        ]},
        {"module": "VLSI Design", "topics": ["CMOS", "Verilog", "FPGA"], "duration": "4 months", "courses": [
            {"platform": "YouTube", "name": "VLSI Design Course", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgVfH0gRi43IVTvH8JjrIKk", "free": True}
        ]}
    ],
    "Electrical and Electronics Engineering": [
        {"module": "Electrical Machines", "topics": ["DC Machines", "Transformers", "Induction Motors"], "duration": "3 months", "courses": [
            {"platform": "YouTube", "name": "Electrical Machines Lectures", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgLRvpp_oe_NnfYWJxeRvJH", "free": True}
        ]},
        {"module": "Power Systems", "topics": ["Generation", "Transmission", "Distribution"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Power Systems", "url": "https://www.coursera.org/learn/power-systems", "free": True},
            {"platform": "YouTube", "name": "Power Systems Course", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgLRvpp_oe_NnfYWJxeRvJH", "free": True}
        ]},
        {"module": "Control Systems", "topics": ["PID Controllers", "State Space", "Stability"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Control Systems Engineering", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRhqzJT87LsdQKYZBC93ezDo", "free": True}
        ]},
        {"module": "Power Electronics", "topics": ["Converters", "Inverters", "Rectifiers"], "duration": "2 months", "courses": [
            {"platform": "YouTube", "name": "Power Electronics Course", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRhqzJT87LsdQKYZBC93ezDo", "free": True}
        ]},
        {"module": "Renewable Energy", "topics": ["Solar", "Wind", "Smart Grid"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Renewable Energy", "url": "https://www.coursera.org/learn/renewable-energy", "free": True}
        ]}
    ],
    "Information Technology": [
        {"module": "Programming Fundamentals", "topics": ["Python", "Java", "C++"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Python for Everybody", "url": "https://www.coursera.org/specializations/python", "free": True},
            {"platform": "YouTube", "name": "FreeCodeCamp Python", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "free": True}
        ]},
        {"module": "Networking Fundamentals", "topics": ["TCP/IP", "Routing", "Network Security"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "Computer Networking", "url": "https://www.coursera.org/learn/computer-networking", "free": True},
            {"platform": "YouTube", "name": "Networking Course", "url": "https://www.youtube.com/watch?v=qiQR5rTSshw", "free": True}
        ]},
        {"module": "Database Management", "topics": ["SQL", "NoSQL", "Database Design"], "duration": "2 months", "courses": [
            {"platform": "Coursera", "name": "SQL for Data Science", "url": "https://www.coursera.org/learn/sql-for-data-science", "free": True}
        ]},
        {"module": "Cloud Computing", "topics": ["AWS", "Azure", "Docker"], "duration": "3 months", "courses": [
            {"platform": "Coursera", "name": "Cloud Computing Basics", "url": "https://www.coursera.org/learn/cloud-computing-basics", "free": True},
            {"platform": "YouTube", "name": "AWS Tutorial", "url": "https://www.youtube.com/watch?v=ulprqHHWlng", "free": True}
        ]},
        {"module": "Cybersecurity", "topics": ["Ethical Hacking", "Cryptography", "Security"], "duration": "4 months", "courses": [
            {"platform": "Coursera", "name": "Cybersecurity Specialization", "url": "https://www.coursera.org/specializations/cyber-security", "free": True},
            {"platform": "YouTube", "name": "Cybersecurity Course", "url": "https://www.youtube.com/watch?v=U_P23SqJaDc", "free": True}
        ]}
    ]
}
