# College type classification based on real Tamil Nadu college names

def get_college_type(college_name):
    """
    Classify college type based on name patterns
    Returns: dict with type, badge, and color
    """
    name_upper = college_name.upper()
    
    # Government colleges - keywords
    government_keywords = [
        "GOVERNMENT", "GOVT", "ANNA UNIVERSITY", 
        "REGIONAL CAMPUS", "UNIVERSITY DEPARTMENTS",
        "COLLEGE OF ENGINEERING GUINDY", "CEG",
        "MADRAS INSTITUTE OF TECHNOLOGY", "MIT",
        "ALAGAPPA COLLEGE", "THANTHAI PERIYAR"
    ]
    
    # Aided colleges - specific well-known aided institutions
    aided_keywords = [
        "PSG", "KUMARAGURU", "KONGU", "BANNARI AMMAN",
        "THIAGARAJAR", "MEPCO", "K.S.RANGASAMY",
        "KAMARAJ", "SETHU", "VELAMMAL", "SRI KRISHNA",
        "KARPAGAM", "SONA", "ADHIYAMAAN"
    ]
    
    # Check for government
    for keyword in government_keywords:
        if keyword in name_upper:
            return {
                "type": "Government",
                "badge": "🏛️ Government",
                "color": "#10b981",  # Green
                "description": "Government-funded institution with subsidized fees"
            }
    
    # Check for aided
    for keyword in aided_keywords:
        if keyword in name_upper:
            return {
                "type": "Aided",
                "badge": "🎓 Aided",
                "color": "#3b82f6",  # Blue
                "description": "Partially government-aided private institution"
            }
    
    # Default to self-financing
    return {
        "type": "Self-Financing",
        "badge": "🏢 Self-Financing",
        "color": "#f59e0b",  # Orange
        "description": "Private institution with higher fees"
    }


# Additional college information
COLLEGE_INFO = {
    "benefits": {
        "Government": [
            "Lowest fees (₹50K-80K per year)",
            "High credibility and reputation",
            "Better infrastructure and facilities",
            "Strong alumni network",
            "Government job preferences"
        ],
        "Aided": [
            "Moderate fees (₹100K-150K per year)",
            "Good balance of quality and cost",
            "Established institutions",
            "Decent placement records",
            "Government support for infrastructure"
        ],
        "Self-Financing": [
            "Fees vary (₹150K-300K per year)",
            "Modern facilities and labs",
            "Industry collaborations",
            "Flexible admission process",
            "Focus on placements"
        ]
    }
}

def get_college_benefits(college_type):
    """Get benefits list for a college type"""
    return COLLEGE_INFO["benefits"].get(college_type, [])
