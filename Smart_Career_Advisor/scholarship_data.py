# Scholarship Database for Indian Engineering Students

SCHOLARSHIPS = [
    {
        "id": 1,
        "name": "Post Matric Scholarship for SC Students",
        "provider": "Government of India",
        "amount": "₹10,000 - ₹20,000/year",
        "eligibility": {
            "category": ["SC"],
            "income": "Family income < ₹2.5 lakh/year",
            "merit": "Pass in previous exam",
            "branch": "All"
        },
        "deadline": "2024-10-31",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Income Certificate", "Caste Certificate", "Previous Marksheet", "Bank Details"],
        "apply_link": "https://scholarships.gov.in/",
        "description": "Central sector scheme for SC students pursuing higher education"
    },
    {
        "id": 2,
        "name": "Post Matric Scholarship for ST Students",
        "provider": "Government of India",
        "amount": "₹10,000 - ₹20,000/year",
        "eligibility": {
            "category": ["ST"],
            "income": "Family income < ₹2.5 lakh/year",
            "merit": "Pass in previous exam",
            "branch": "All"
        },
        "deadline": "2024-10-31",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Income Certificate", "Tribe Certificate", "Previous Marksheet", "Bank Details"],
        "apply_link": "https://scholarships.gov.in/",
        "description": "Central sector scheme for ST students pursuing higher education"
    },
    {
        "id": 3,
        "name": "Post Matric Scholarship for OBC Students",
        "provider": "Government of India",
        "amount": "₹5,000 - ₹15,000/year",
        "eligibility": {
            "category": ["BC", "BCM", "MBC"],
            "income": "Family income < ₹1 lakh/year",
            "merit": "Pass in previous exam",
            "branch": "All"
        },
        "deadline": "2024-11-15",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Income Certificate", "OBC Certificate", "Previous Marksheet", "Bank Details"],
        "apply_link": "https://scholarships.gov.in/",
        "description": "Financial assistance for OBC students in higher education"
    },
    {
        "id": 4,
        "name": "National Means cum Merit Scholarship",
        "provider": "Ministry of Education",
        "amount": "₹12,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹3.5 lakh/year",
            "merit": "Minimum 60% in previous exam",
            "branch": "All"
        },
        "deadline": "2024-09-30",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Domicile Certificate", "Bank Details"],
        "apply_link": "https://scholarships.gov.in/",
        "description": "Merit-based scholarship for economically weaker students"
    },
    {
        "id": 5,
        "name": "AICTE Pragati Scholarship for Girls",
        "provider": "AICTE",
        "amount": "₹50,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹8 lakh/year",
            "merit": "Minimum 60% in 12th",
            "branch": "All Engineering"
        },
        "deadline": "2024-10-15",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Income Certificate", "12th Marksheet", "Admission Proof", "Bank Details"],
        "apply_link": "https://www.aicte-india.org/",
        "description": "Encouraging girl students in technical education"
    },
    {
        "id": 6,
        "name": "AICTE Saksham Scholarship for Disabled",
        "provider": "AICTE",
        "amount": "₹50,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹8 lakh/year",
            "merit": "Minimum 60% in 12th",
            "branch": "All Engineering"
        },
        "deadline": "2024-10-15",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Disability Certificate", "Income Certificate", "12th Marksheet", "Bank Details"],
        "apply_link": "https://www.aicte-india.org/",
        "description": "Supporting differently-abled students in technical education"
    },
    {
        "id": 7,
        "name": "Tamil Nadu First Graduate Scholarship",
        "provider": "Government of Tamil Nadu",
        "amount": "₹15,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹2 lakh/year",
            "merit": "Pass in 12th",
            "branch": "All"
        },
        "deadline": "2024-11-30",
        "type": "State",
        "first_graduate": True,
        "documents": ["First Graduate Certificate", "Income Certificate", "12th Marksheet", "Community Certificate"],
        "apply_link": "https://www.tn.gov.in/",
        "description": "Special scholarship for first-generation graduates in Tamil Nadu"
    },
    {
        "id": 8,
        "name": "Dr. Ambedkar Post Matric Scholarship",
        "provider": "Government of Tamil Nadu",
        "amount": "₹10,000 - ₹25,000/year",
        "eligibility": {
            "category": ["SC"],
            "income": "Family income < ₹2.5 lakh/year",
            "merit": "Pass in previous exam",
            "branch": "All"
        },
        "deadline": "2024-10-31",
        "type": "State",
        "first_graduate": False,
        "documents": ["SC Certificate", "Income Certificate", "Previous Marksheet", "Bank Details"],
        "apply_link": "https://www.tn.gov.in/",
        "description": "Tamil Nadu state scholarship for SC students"
    },
    {
        "id": 9,
        "name": "Inspire Scholarship for Higher Education",
        "provider": "Department of Science & Technology",
        "amount": "₹80,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "No income limit",
            "merit": "Top 1% in 12th board exam",
            "branch": "All Engineering & Science"
        },
        "deadline": "2024-09-15",
        "type": "Government",
        "first_graduate": False,
        "documents": ["12th Marksheet", "Admission Proof", "Bank Details", "Aadhar Card"],
        "apply_link": "https://online-inspire.gov.in/",
        "description": "Merit-based scholarship for top performers in science stream"
    },
    {
        "id": 10,
        "name": "Sitaram Jindal Foundation Scholarship",
        "provider": "Sitaram Jindal Foundation",
        "amount": "₹20,000 - ₹50,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹5 lakh/year",
            "merit": "Minimum 60% in previous exam",
            "branch": "All Engineering"
        },
        "deadline": "2024-08-31",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Admission Proof", "Bank Details"],
        "apply_link": "https://www.sitaramjindalfoundation.org/",
        "description": "Supporting meritorious students from economically weaker sections"
    },
    {
        "id": 11,
        "name": "Reliance Foundation Scholarship",
        "provider": "Reliance Foundation",
        "amount": "₹2,00,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹6 lakh/year",
            "merit": "Minimum 60% in 12th",
            "branch": "All Engineering"
        },
        "deadline": "2024-07-31",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "12th Marksheet", "Admission Proof", "Essay"],
        "apply_link": "https://www.reliancefoundation.org/",
        "description": "Comprehensive scholarship covering tuition and living expenses"
    },
    {
        "id": 12,
        "name": "Tata Capital Pankh Scholarship",
        "provider": "Tata Capital",
        "amount": "₹10,000 - ₹12,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹4 lakh/year",
            "merit": "Minimum 60% in previous exam",
            "branch": "All"
        },
        "deadline": "2024-09-30",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Admission Proof", "Bank Details"],
        "apply_link": "https://www.buddy4study.com/",
        "description": "Supporting students from economically disadvantaged backgrounds"
    },
    {
        "id": 13,
        "name": "LIC Golden Jubilee Scholarship",
        "provider": "Life Insurance Corporation",
        "amount": "₹20,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹2.5 lakh/year",
            "merit": "Minimum 60% in previous exam",
            "branch": "All"
        },
        "deadline": "2024-08-15",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Admission Proof", "Bank Details"],
        "apply_link": "https://www.licindia.in/",
        "description": "Financial assistance for meritorious students from low-income families"
    },
    {
        "id": 14,
        "name": "Vahani Scholarship for Women",
        "provider": "Vahani Scholarship Trust",
        "amount": "₹15,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹3 lakh/year",
            "merit": "Minimum 50% in previous exam",
            "branch": "All Engineering"
        },
        "deadline": "2024-10-31",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Admission Proof", "Bank Details"],
        "apply_link": "https://www.buddy4study.com/",
        "description": "Empowering women in technical education"
    },
    {
        "id": 15,
        "name": "Swami Vivekananda Merit Scholarship",
        "provider": "Government of West Bengal",
        "amount": "₹1,000/month",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹2.5 lakh/year",
            "merit": "Top 75% in qualifying exam",
            "branch": "All"
        },
        "deadline": "2024-11-30",
        "type": "State",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Domicile Certificate", "Bank Details"],
        "apply_link": "https://svmcm.wbhed.gov.in/",
        "description": "Merit-cum-means scholarship for students in West Bengal"
    },
    {
        "id": 16,
        "name": "Minority Scholarship for Engineering",
        "provider": "Ministry of Minority Affairs",
        "amount": "₹20,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹2 lakh/year",
            "merit": "Minimum 50% in previous exam",
            "branch": "All Engineering"
        },
        "deadline": "2024-10-31",
        "type": "Government",
        "first_graduate": False,
        "documents": ["Minority Certificate", "Income Certificate", "Marksheet", "Bank Details"],
        "apply_link": "https://scholarships.gov.in/",
        "description": "Supporting minority community students in technical education"
    },
    {
        "id": 17,
        "name": "Colgate Keep India Smiling Scholarship",
        "provider": "Colgate-Palmolive",
        "amount": "₹50,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹5 lakh/year",
            "merit": "Minimum 60% in previous exam",
            "branch": "All"
        },
        "deadline": "2024-09-30",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "Marksheet", "Admission Proof", "Essay"],
        "apply_link": "https://www.buddy4study.com/",
        "description": "Supporting underprivileged students across India"
    },
    {
        "id": 18,
        "name": "Narotam Sekhsaria Foundation Scholarship",
        "provider": "Narotam Sekhsaria Foundation",
        "amount": "₹50,000 - ₹2,00,000/year",
        "eligibility": {
            "category": ["All"],
            "income": "Family income < ₹4.5 lakh/year",
            "merit": "Minimum 60% in 12th",
            "branch": "All Engineering"
        },
        "deadline": "2024-08-31",
        "type": "Private",
        "first_graduate": False,
        "documents": ["Income Certificate", "12th Marksheet", "Admission Proof", "Recommendation Letter"],
        "apply_link": "https://www.nsfoundation.co.in/",
        "description": "Comprehensive support for academically bright students"
    }
]

# Success stories for motivation
SUCCESS_STORIES = [
    {
        "name": "Priya Sharma",
        "scholarship": "AICTE Pragati Scholarship",
        "branch": "Computer Science and Engineering",
        "story": "First-generation graduate from a rural area. The scholarship helped me complete my B.Tech without financial burden. Now working at a top IT company!",
        "year": "2023"
    },
    {
        "name": "Rajesh Kumar",
        "scholarship": "Tamil Nadu First Graduate Scholarship",
        "branch": "Mechanical Engineering",
        "story": "Being the first graduate in my family, this scholarship was a blessing. It covered my fees and books. Today, I'm an engineer at an automobile company.",
        "year": "2022"
    },
    {
        "name": "Anitha M",
        "scholarship": "Post Matric Scholarship for SC",
        "branch": "Civil Engineering",
        "story": "From a small village with limited resources, this scholarship made my engineering dream possible. Now I'm helping build infrastructure for my community.",
        "year": "2023"
    },
    {
        "name": "Mohammed Farhan",
        "scholarship": "Minority Scholarship",
        "branch": "Bio Medical Engineering",
        "story": "The scholarship not only provided financial support but also boosted my confidence. Currently pursuing research in medical devices.",
        "year": "2022"
    }
]
