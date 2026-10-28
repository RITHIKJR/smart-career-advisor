import streamlit as st
import pandas as pd
import pickle
from database import init_db, register_user, login_user

# ==============================
# INITIALIZE DATABASE
# ==============================

init_db()

# ==============================
# SESSION STATE
# ==============================

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

# ==============================
# LOAD MODEL & DATA
# ==============================

model = pickle.load(open("college_model.pkl", "rb"))
data = pd.read_csv("tnea_cutoff_clean.csv")

data.columns = data.columns.str.strip()

college_code_col = "college_code"
college_name_col = "college"
branch_col = "branch"

category_columns = ["OC", "BC", "BCM", "MBC", "SC", "SCA", "ST"]

long_data = data.melt(
    id_vars=[college_code_col, college_name_col, branch_col],
    value_vars=category_columns,
    var_name="Category",
    value_name="Required_Cutoff"
)

long_data = long_data.dropna()

# ==============================
# STREAMLIT UI
# ==============================

st.set_page_config(page_title="Smart Career Advisor", layout="wide")

st.title("🎓 Smart Career Guidance & Learning Path Advisor")

# ==============================
# LOGIN/REGISTER
# ==============================

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login")
        login_username = st.text_input("Username", key="login_user")
        login_password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Login"):
            if login_user(login_username, login_password):
                st.session_state.logged_in = True
                st.session_state.username = login_username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    with tab2:
        st.subheader("Register")
        reg_username = st.text_input("Username", key="reg_user")
        reg_email = st.text_input("Email", key="reg_email")
        reg_password = st.text_input("Password", type="password", key="reg_pass")
        reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
        
        if st.button("Register"):
            if reg_password != reg_confirm:
                st.error("Passwords do not match")
            elif len(reg_password) < 6:
                st.error("Password must be at least 6 characters")
            elif register_user(reg_username, reg_email, reg_password):
                st.success("Registration successful! Please login.")
            else:
                st.error("Username or email already exists")
    st.stop()

# ==============================
# MAIN APP (After Login)
# ==============================

col1, col2 = st.columns([6, 1])
with col1:
    st.write(f"Welcome, **{st.session_state.username}**!")
with col2:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.rerun()

st.header("Enter Your Details")

cutoff = st.number_input("Enter Your Cutoff", min_value=0.0, max_value=200.0)
category = st.selectbox("Select Category", category_columns)
branch = st.selectbox("Interested Branch", ["CSE", "IT", "ECE", "MECH", "CIVIL", "EEE", "AI"])

if st.button("Get College Recommendation"):

    branch_map = {
        "CSE": "COMPUTER SCIENCE",
        "ECE": "ELECTRONICS",
        "MECH": "MECHANICAL",
        "CIVIL": "CIVIL",
        "IT": "INFORMATION TECHNOLOGY",
        "EEE": "ELECTRICAL",
        "AI": "ARTIFICIAL INTELLIGENCE"
    }

    branch_keyword = branch_map.get(branch, branch)

    recommendations = []

    for _, row in long_data.iterrows():

        if category != row["Category"]:
            continue

        if branch_keyword not in str(row[branch_col]).upper():
            continue

        required_cutoff = row["Required_Cutoff"]

        input_dict = {
            "Student_Cutoff": cutoff,
            "Required_Cutoff": required_cutoff
        }

        for col in model.feature_names_in_:
            if col.startswith("Category_"):
                input_dict[col] = 1 if col == f"Category_{category}" else 0

        input_df = pd.DataFrame([input_dict])

        probability = model.predict_proba(input_df)[0][1]

        recommendations.append((
            probability,
            row[college_code_col],
            row[college_name_col],
            row[branch_col],
            required_cutoff
        ))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    if len(recommendations) == 0:
        st.error("No colleges found for your criteria ❌")
    else:
        st.success("Top Recommended Colleges 🔥")

        for rec in recommendations[:10]:
            st.write(f"**{rec[1]} - {rec[2]}**")
            st.write(f"Branch: {rec[3]}")
            st.write(f"Required Cutoff: {rec[4]}")
            st.write(f"Admission Probability: {round(rec[0]*100,2)}%")
            st.write("---")
