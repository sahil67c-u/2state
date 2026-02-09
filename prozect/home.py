import streamlit as st
import os
from streamlit_extras.let_it_rain import rain

# 1. Page Config
st.set_page_config(
    page_title="For Chiku ❤️",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 2. INITIALIZE SESSION STATE (MUST BE AT THE TOP)
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
    /* Hide the default Streamlit Sidebar */
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
# 4. TOP NAVIGATION BAR
# ---------------------------------------------------------
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
# ---------------------------------------------------------
# 5. PAGE CONTENT (LOGIC)
# ---------------------------------------------------------

# --- STAGE 0: Intro ---
if st.session_state.stage == 0:
    st.title("Hey Chiku! 👋")
    # Using the direct link that usually works better
    st.video("vdo3.mp4", format="video/mp4", start_time=0) 
    
    st.markdown("<h3>I have something really serious to ask you...</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Yes, go ahead! 😤"):
            st.session_state.stage = 1
            st.rerun()

# --- STAGE 1: The Question ---
elif st.session_state.stage == 1:
    st.title("Okay, here goes nothing... 🫣")
    st.video("vdo2.mp4", format="video/mp4", start_time=0) 
    
    st.markdown("<h1>WILL YOU BE MY VALENTINE? 🌹</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! Of course! ❤️"):
            st.session_state.stage = 2
            st.rerun()
    with col2:
        no_texts = ["No", "Are you sure?", "Don't do this 🥺", "I'm gonna cry...", "Just click YES!"]
        # Cycle through texts
        text_index = min(st.session_state.no_count, len(no_texts)-1)
        
        if st.button(no_texts[text_index]):
            st.session_state.no_count += 1
            st.rerun()

# --- STAGE 2: Success ---
elif st.session_state.stage == 2:
    st.title("YEAYYY! I KNEW IT! 🎉❤️")
    
    # MAGIC FIX: File ko sahi jagah dhoondne ka code
    current_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(current_dir, "vdo3.mp4")

    # Check karega agar video mili ya nahi
    if os.path.exists(video_path):
        st.video(video_path, format="video/mp4", start_time=0)
    else:
        # Fallback agar tab bhi na mile
        st.error(f"Video not found at: {video_path}")
        st.image("https://media.tenor.com/26BRv0ThflsHCqDrG/giphy.gif") # Backup GIF
    
    st.markdown("<h3>Now go check the Gallery page! 👆</h3>", unsafe_allow_html=True)
    
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
