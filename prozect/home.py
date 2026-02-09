import streamlit as st
import os  # <--- Ye zaroori hai path dhundne ke liye
from streamlit_extras.let_it_rain import rain

# 1. Page Config
st.set_page_config(
    page_title="For Chiku ❤️",
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
    [data-testid="stSidebarNav"] {display: none;}
    .stApp {background-color: #ffe6e6;}
    h1, h2, h3, p, div, span {
        color: #4a0010 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: 800 !important;
    }
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
    st.title("Hey Chiku! 👋")
    # Updated Working GIF
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
    # Updated Working GIF
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

# --- STAGE 2: Success (THE FIXED PART) ---
elif st.session_state.stage == 2:
    st.title("YEAYYY! I KNEW IT! 🎉❤️")
    
    # --- MAGIC PATH FIX ---
    # Ye code current file ka folder pata karega aur wahin video dhundega
    current_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(current_dir, "vdo3.mp4")
    
    # Debugging ke liye: Agar error aaye toh ye batayega ki wo kya dhund raha tha
    if os.path.exists(video_path):
        st.video(video_path, format="video/mp4", start_time=0)
    else:
        st.error(f"Video file nahi mili! Main yahan dhund raha tha: {video_path}")
        st.warning("Make sure 'vdo3.mp4' 'home.py' ke saath same folder mein hai.")
        # Backup GIF agar video na chale
        st.image("https://media.tenor.com/26BRv0ThflsHCqDrG/giphy.gif")
    
    st.markdown("<h3>Now go check the Gallery page! 👆</h3>", unsafe_allow_html=True)
    
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
