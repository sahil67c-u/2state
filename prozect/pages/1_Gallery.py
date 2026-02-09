import streamlit as st
import os  # <--- Ye line zaroori hai path dhundne ke liye

# 1. Page Config
st.set_page_config(page_title="Our Memories 📸", page_icon="🎞️", layout="wide", initial_sidebar_state="collapsed")

# 2. THEME & STYLING
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    .stApp {background-color: #ffe6e6;}
    h1, h2, h3, h4, p, div, span {
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
    .song-tag {
        font-size: 1rem;
        color: #fff !important;
        background-color: #ff4b4b;
        padding: 5px 15px;
        border-radius: 20px;
        border: 2px solid #330000;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOP NAVIGATION
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

# ================= PAGE CONTENT =================

st.title("📸 The 'Chiku' Museum")
st.markdown("### Every picture tells a story... (and a song!) 🎶")
st.write("")

# --- MAGIC PATH SETUP ---
# Ye current file (Gallery.py) ka folder pata karega
current_dir = os.path.dirname(os.path.abspath(__file__))
# Ye uske ek level upar jayega (Jahan p1.jpg rakha hai)
parent_dir = os.path.dirname(current_dir)

# MEMORY DATA
memories = [
    {"img": "p1.jpg", "lyric": "Tera hone laga hoon... 🥰", "song": "Tera Hone Laga Hoon"},
    {"img": "p2.jpg", "lyric": "Tujh mein rab dikhta hai... 🙏❤️", "song": "Tujh Mein Rab Dikhta Hai"},
    {"img": "p3.jpg", "lyric": "Tum se hi din hota hai... 🌅", "song": "Tum Se Hi"},
    {"img": "p4.jpg", "lyric": "Kaise hua, tu itna zaroori? 🤔💘", "song": "Kaise Hua"},
    {"img": "p5.jpg", "lyric": "Main rang sharbaton ka... 🍬", "song": "Tera Yaar Hoon Main"},
    {"img": "p6.jpg", "lyric": "Raataan lambiyan lambiyan re... 🌙", "song": "Raataan Lambiyan"},
    {"img": "p7.jpg", "lyric": "Agar tum saath ho... 💪🌍", "song": "Agar Tum Saath Ho"},
    {"img": "p8.jpg", "lyric": "Kesariya tera ishq hai piya... 🧡", "song": "Kesariya"},
    {"img": "p9.jpg", "lyric": "Apna bana le piya... 🤗", "song": "Apna Bana Le"},
    {"img": "p10.jpg", "lyric": "Subhanallah... 😍", "song": "Subhanallah"}
]

# LOOP FOR LAYOUT
for i, item in enumerate(memories):
    
    # Path Construction: Parent Folder + Image Name
    img_path = os.path.join(parent_dir, item["img"])
    
    if i % 2 == 0:
        c1, c2 = st.columns([1.5, 2], gap="medium")
        with c1:
            st.markdown(f"## Memory #{i+1}")
            st.markdown(f"#### {item['lyric']}")
            st.markdown(f"<div class='song-tag'>🎵 {item['song']}</div>", unsafe_allow_html=True)
        with c2:
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.error(f"⚠️ Image not found at: {img_path}")
    else:
        c1, c2 = st.columns([2, 1.5], gap="medium")
        with c1:
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.error(f"⚠️ Image not found at: {img_path}")
        with c2:
            st.markdown(f"## Memory #{i+1}")
            st.markdown(f"#### {item['lyric']}")
            st.markdown(f"<div class='song-tag'>🎵 {item['song']}</div>", unsafe_allow_html=True)

    st.write("---")

st.markdown("<h3 style='text-align: center;'>See? I told you, crazy obsessed. 🤪</h3>", unsafe_allow_html=True)
