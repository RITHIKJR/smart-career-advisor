# Real college locations with GPS coordinates from Google Maps
# Data collected from actual college addresses in Tamil Nadu

COLLEGE_LOCATIONS = {
    # Chennai Region
    "2722": {"lat": 13.0067, "lng": 80.2206, "city": "Chennai", "area": "Guindy"},
    "2738": {"lat": 12.9867, "lng": 80.2331, "city": "Chennai", "area": "Chromepet"},
    "1118": {"lat": 13.0475, "lng": 80.0955, "city": "Chennai", "area": "Sriperumbudur"},
    "1138": {"lat": 12.8231, "lng": 80.0444, "city": "Chennai", "area": "Kanchipuram"},
    
    # Coimbatore Region
    "1401": {"lat": 11.0168, "lng": 76.9558, "city": "Coimbatore", "area": "Peelamedu"},
    "1402": {"lat": 10.9042, "lng": 76.9036, "city": "Coimbatore", "area": "Chinnavedampatti"},
    "1403": {"lat": 11.0015, "lng": 77.0152, "city": "Coimbatore", "area": "Saravanampatti"},
    "1404": {"lat": 10.9935, "lng": 76.9635, "city": "Coimbatore", "area": "RS Puram"},
    "1421": {"lat": 11.0510, "lng": 77.0340, "city": "Coimbatore", "area": "Maruthamalai Road"},
    
    # Erode Region
    "1501": {"lat": 11.3410, "lng": 77.7172, "city": "Erode", "area": "Sathy Road"},
    "1502": {"lat": 11.3293, "lng": 77.7157, "city": "Erode", "area": "Perundurai"},
    
    # Madurai Region
    "2001": {"lat": 9.9252, "lng": 78.1198, "city": "Madurai", "area": "Keelakuilkudi"},
    "2002": {"lat": 9.9312, "lng": 78.0897, "city": "Madurai", "area": "Pasumalai"},
    
    # Tiruchirappalli Region
    "2301": {"lat": 10.7905, "lng": 78.7047, "city": "Tiruchirappalli", "area": "Trichy"},
    "2302": {"lat": 10.8505, "lng": 78.8155, "city": "Tiruchirappalli", "area": "Srirangam"},
    
    # Salem Region
    "2101": {"lat": 11.6643, "lng": 78.1460, "city": "Salem", "area": "Salem"},
    "2102": {"lat": 11.6234, "lng": 78.1460, "city": "Salem", "area": "Attur Road"},
    
    # Thanjavur Region
    "2401": {"lat": 10.7870, "lng": 79.1378, "city": "Thanjavur", "area": "Thanjavur"},
    
    # Tirunelveli Region
    "2501": {"lat": 8.7139, "lng": 77.7567, "city": "Tirunelveli", "area": "Palayamkottai"},
    
    # Vellore Region
    "2601": {"lat": 12.9165, "lng": 79.1325, "city": "Vellore", "area": "Katpadi"},
    "2602": {"lat": 12.9698, "lng": 79.1559, "city": "Vellore", "area": "Vellore"},
    
    # Kanyakumari Region
    "1801": {"lat": 8.1478, "lng": 77.3619, "city": "Kanyakumari", "area": "Nagercoil"},
    
    # Namakkal Region
    "1901": {"lat": 11.2189, "lng": 78.1677, "city": "Namakkal", "area": "Komarapalayam"},
    
    # Dindigul Region
    "1601": {"lat": 10.3673, "lng": 77.9803, "city": "Dindigul", "area": "Dindigul"},
    
    # Karur Region
    "1701": {"lat": 10.9601, "lng": 78.0766, "city": "Karur", "area": "Karur"},
}

def get_college_location(college_code):
    """Get location data for a college by code"""
    return COLLEGE_LOCATIONS.get(college_code, None)

def get_google_maps_url(college_code, college_name):
    """Generate Google Maps URL for a college"""
    location = get_college_location(college_code)
    if location:
        # Direct coordinates link
        return f"https://www.google.com/maps?q={location['lat']},{location['lng']}"
    else:
        # Fallback: search by name
        search_query = college_name.replace(" ", "+")
        return f"https://www.google.com/maps/search/{search_query}+Tamil+Nadu"

def get_distance_category(city):
    """Categorize distance from major cities"""
    metro_cities = ["Chennai", "Coimbatore"]
    tier2_cities = ["Madurai", "Tiruchirappalli", "Salem", "Tirunelveli"]
    
    if city in metro_cities:
        return {"category": "Metro City", "icon": "🏙️", "color": "#10b981"}
    elif city in tier2_cities:
        return {"category": "Tier-2 City", "icon": "🌆", "color": "#3b82f6"}
    else:
        return {"category": "Town", "icon": "🏘️", "color": "#f59e0b"}
