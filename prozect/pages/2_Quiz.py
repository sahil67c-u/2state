import streamlit as st
import time

# 1. Page Config
st.set_page_config(page_title="The Hardest Test 📝", page_icon="🧐", layout="centered", initial_sidebar_state="collapsed")

# 2. THEME & NAVIGATION (Matches other pages)
st.markdown("""
    <style>
    /* Hide Sidebar */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Pink Background */
    .stApp {
        background-color: #ffe6e6;
    }
    
    /* Text Styling - Dark Maroon & Bold */
    h1, h2, h3, h4, p, label, div {
        color: #4a0010 !important; 
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: 800 !important;
    }
    
    /* Radio Button Text */
    .stRadio > label {
        font-size: 1.2rem !important;
    }
    
    /* Buttons */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white !important;
        border-radius: 10px;
        border: 2px solid #330000;
        font-weight: bold;
        width: 100%;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOP NAVIGATION BAR
col1, col2, col3, col4, col5 = st.columns(5, gap="small")
with col1:
    if st.button("🏠", help="Home", use_container_width=True): st.switch_page("home.py")
with col2:
    if st.button("📸", help="Gallery", use_container_width=True): st.switch_page("pages/1_Gallery.py")
with col3:
    if st.button("🧐", help="Quiz", use_container_width=True): st.switch_page("pages/2_Quiz.py")
with col4:
    if st.button("🎟️", help="Coupons", use_container_width=True): st.switch_page("pages/3_Coupons.py")
with col5:
    if st.button("💌", help="Letters", use_container_width=True): st.switch_page("pages/4_Letter.py")

st.write("---")

# ================= QUIZ LOGIC =================

st.title("🧐 How well do you know me?")
st.markdown("### If you score less than 5/5, no chocolates for you. 😤")

# --- DEFINE YOUR QUESTIONS HERE ---
# Format: "Question": ["Option 1", "Option 2", "Option 3", "Correct Option"]
quiz_data = {
    "1. What is my favorite food? 🍕": [
        "Pizza", 
        "Paneer Chilli", 
        "Kaju paneer", 
        "Paneer Chilli"  # <--- Change this to the real correct answer
    ],
    "2. When is my birthday? 🎂": [
        "February 19", 
        "August 9", 
        "April 2", 
        "August 9" # <--- Change this
    ],
    "3. Which color suits me best? 👗": [
        "Red", 
        "Black", 
        "Baby Pink", 
        "Baby Pink" # <--- Change this
    ],
    "4. What makes me most angry? 😡": [
        "Slow replies", 
        "Bad food", 
        "Cancelling plans", 
        "Bad food" # <--- Change this
    ],
    "5. Who is my favorite person? (Be careful) 👀": [
        "Mumma", 
        "You (Gaurav)", 
        "Papa", 
        "You (Gaurav)" # <--- Change this
    ]
}

# Iterate through questions and store answers
score = 0
user_answers = {}

# Create the form
with st.form("quiz_form"):
    for question, options in quiz_data.items():
        st.write("")
        st.markdown(f"#### {question}")
        # The last item in the list is the correct answer, so we exclude it from options displayed
        display_options = options[:-1] 
        user_answers[question] = st.radio(f"Select answer for: {question}", display_options, index=None, label_visibility="collapsed")
        st.write("---")

    submit_button = st.form_submit_button("Submit Answers 🔒")

# --- RESULT CHECKING ---
if submit_button:
    correct_count = 0
    
    for question, options in quiz_data.items():
        correct_answer = options[-1] # The last item we hid is the correct one
        user_choice = user_answers[question]
        
        if user_choice == correct_answer:
            correct_count += 1

    # DISPLAY RESULT
    if correct_count == 5:
        st.balloons()
        st.title(f"Score: {correct_count}/5 🎉")
        st.success("OMG! You actually pay attention! You are the best Valentine ever! ❤️")
        st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif") # Happy Hug
    elif correct_count >= 3:
        st.warning(f"Score: {correct_count}/5 😐")
        st.markdown("### Not bad... but you can do better.")
        st.image("https://media.giphy.com/media/VbnUQpnihPSlIxeUUk/giphy.gif") # Skeptical face
    else:
        st.error(f"Score: {correct_count}/5 💀")
        st.markdown("### ARE YOU SERIOUS? WE NEED TO TALK.")
        st.image("https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif") # Crying/Angry