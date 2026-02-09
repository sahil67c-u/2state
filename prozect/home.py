import streamlit as st
import os  # <--- Path dhundne ke liye zaroori
from streamlit_extras.let_it_rain import rain

# 1. Page Config
st.set_page_config(
    page_title="For Gaurav ❤️",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 2. INITIALIZE SESSION STATE
# ---------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 0

if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

# ---------------------------------------------------------
# 3. CSS & STYLING
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Hide Default Sidebar */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Pink Background */
    .stApp {
        background-color: #ffe6e6;
    }
    
    /* Text Styling */
    h1, h2, h3, p, div, span {
        color: #4a0010 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: 800 !important;
    }
    
    /* Buttons */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white !important;
        border-radius: 10px;
        border: 2px solid #330000;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. TOP NAVIGATION BAR (5 Icons)
# ---------------------------------------------------------
col1, col2, col3, col4, col5 = st.columns(5, gap="small")
with col1:
    if st.button("🏠", use_container_width=True): st.switch_page("home.py")
with col2:
    if st.button("📸", use_container_width=True): st.switch_page("pages/1_Gallery.py")
with col3:
    if st.button("🧐", use_container_width=True): st.switch_page("pages/2_Quiz.py")
with col4:
    if st.button("🎟️", use_container_width=True): st.switch_page("pages/3_Coupons.py")
with col5:
    if st.button("💌", use_container_width=True): st.switch_page("pages/4_Letter.py")

st.write("---")

# ---------------------------------------------------------
# 5. PAGE CONTENT (LOGIC)
# ---------------------------------------------------------

# --- STAGE 0: Intro ---
if st.session_state.stage == 0:
    st.title("Hey Gaurav! 👋")
    
    # FIX: New Tenor Link (Waving Bear) - Will work 100%
    st.image("https://media.tenor.com/On7kvXhzml4AAAAj/loading-chud.gif", width=200)
    
    st.markdown("<h3>I have something really serious to ask you...</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Yes, go ahead! 😤"):
            st.session_state.stage = 1
            st.rerun()

# --- STAGE 1: The Question ---
elif st.session_state.stage == 1:
    st.title("Okay, here goes nothing... 🫣")
    
    # FIX: New Tenor Link (Nervous/Begging)
    st.image("https://media.tenor.com/Mbf0X7eQyWAAAAAj/peach-goma-peach-and-goma.gif", width=200)
    
    st.markdown("<h1>WILL YOU BE MY VALENTINE? 🌹</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! Of course! ❤️"):
            st.session_state.stage = 2
            st.rerun()
    with col2:
        no_texts = ["No", "Are you sure?", "Don't do this 🥺", "I'm gonna cry...", "Just click YES!"]
        text_index = min(st.session_state.no_count, len(no_texts)-1)
        
        if st.button(no_texts[text_index]):
            st.session_state.no_count += 1
            st.rerun()

# --- STAGE 2: Success (VIDEO FIX) ---
elif st.session_state.stage == 2:
    st.title("YEAYYY! I KNEW IT! 🎉❤️")
    
    # --- MAGIC PATH FIX FOR VIDEO ---
    # 1. Pata karo ki ye script kahan rakhi hai
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 2. Usi folder mein video file dhundo
    video_path = os.path.join(current_dir, "vdo3.mp4") 
    
    # 3. Check karo aur play karo
    if os.path.exists(video_path):
        st.video(video_path, format="video
