import streamlit as st
import os  # <--- Zaroori hai video dhundne ke liye
from streamlit_extras.let_it_rain import rain

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="For Chiku ❤️",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 2. SETUP VIDEO PATHS (Universal Fix)
# ---------------------------------------------------------
# Ye code current folder ka pata lagayega
current_dir = os.path.dirname(os.path.abspath(__file__))

# Teeno videos ke paths set kar diye
vdo1_path = os.path.join(current_dir, "vdo1.mp4")
vdo2_path = os.path.join(current_dir, "vdo2.mp4")
vdo3_path = os.path.join(current_dir, "vdo3.mp4")

# ---------------------------------------------------------
# 3. CSS & STYLING
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Sidebar Hide */
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
# 5. PAGE LOGIC (State Management)
# ---------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 0

if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

# --- STAGE 0: Intro ---
if st.session_state.stage == 0:
    st.title("Hey Chiku! 👋")
    
    # Working Tenor GIF
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
    
    # Working Tenor GIF
    st.image("https://media.tenor.com/Mbf0X7eQyWAAAAAj/peach-goma-peach-and-goma.gif", width=200)
    
    st.markdown("<h1>WILL YOU BE MY VALENTINE? 🌹</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! Of course! ❤️"):
            st.session_state.stage = 2
            st.rerun()
    with col2:
        no_texts = ["No", "Are you sure?", "Don't do this 🥺", "I'm gonna cry...", "Just click YES!"]
        # Button text change logic
        text_index = min(st.session_state.no_count, len(no_texts)-1)
        
        if st.button(no_texts[text_index]):
            st.session_state.no_count += 1
            st.rerun()

# --- STAGE 2: Success (Video Player) ---
elif st.session_state.stage == 2:
    st.title("YEAYYY! I KNEW IT! 🎉❤️")
    
    # -------------------------------------------------
    # VIDEO LOGIC (Change vdo1_path to vdo2_path if needed)
    # -------------------------------------------------
    video_to_play = vdo1_path  # <--- Change this to vdo2_path or vdo3_path if you want
    
    if os.path.exists(video_to_play):
        st.video(video_to_play, format="video/mp4", start_time=0)
    else:
        st.error(f"Video file not found: {video_to_play}")
        # Fallback GIF
        st.image("https://media.tenor.com/26BRv0ThflsHCqDrG/giphy.gif")
    
    st.markdown("<h3>Now go check the Gallery page! 👆</h3>", unsafe_allow_html=True)
    
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
