import streamlit as st

# 1. Page Config (Same as Home)
st.set_page_config(page_title="Our Memories 📸", page_icon="🎞️", layout="wide", initial_sidebar_state="collapsed")

# 2. THEME & HIDE SIDEBAR (Exact copy from Home)
st.markdown("""
    <style>
    /* Hide the default Sidebar */
    [data-testid="stSidebarNav"] {display: none;}

    /* Background Color */
    .stApp {
        background-color: #ffe6e6;
    }

    /* Text Styling - Dark Maroon & Bold */
    h1, h2, h3, h4, p, div, span {
        color: #4a0010 !important; 
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: 800 !important; /* Extra Bold */
    }

    /* Navigation Buttons */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white !important;
        border-radius: 10px;
        border: 2px solid #330000;
        font-weight: bold;
    }
    
    /* Song Tag Styling */
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

# ================= PAGE CONTENT STARTS HERE =================

st.title("📸 The 'Chiku' Museum")
st.markdown("### Every picture tells a story... (and a song!) 🎶")
st.write("") # Spacer

# MEMORY DATA (Update your filenames here)
memories = [
    {"img": "p1.jpg", "lyric": "Tera hone laga hoon... 🥰", "song": "Tera Hone Laga Hoon"},
    {"img": "p2.jpg", "lyric": "Tujh mein rab dikhta hai... 🙏❤️", "song": "Tujh Mein Rab Dikhta Hai"},
    {"img": "p3.jpg", "lyric": "Tum se hi din hota hai... 🌅", "song": "Tum Se Hi"},
    {"img": "p4.jpg", "lyric": "Kaise hua, tu itna zaroori? 🤔💘", "song": "Kaise Hua"},
    {"img": "p5.jpg", "lyric": "Main rang sharbaton ka... 🍬", "song": "Tera Yaar Hoon Main"},
    {"img": "p6.jpg", "lyric": "Inn aankhon se ye bata Kitna main dekhu tujhe Reh jaati hai kuch kami Jitna bhi dekhu tujhe 🌙", "song": "Rojana"},
    {"img": "p7.jpg", "lyric": "Agar tum saath ho... 💪🌍", "song": "Agar Tum Saath Ho"},
    {"img": "p8.jpg", "lyric": "Kesariya tera ishq hai piya... 🧡", "song": "Kesariya"},
    {"img": "p9.jpg", "lyric": "Apna bana le piya... 🤗", "song": "Apna Bana Le"},
    {"img": "p10.jpg", "lyric": "Meri wafaa pe haq hua tera\nLo main qayamat tak hua tera😍", "song": "Subhanallah"}
]

# LOOP FOR LAYOUT
for i, item in enumerate(memories):
    
    # Create alternating layout
    if i % 2 == 0:
        # Text Left | Photo Right
        c1, c2 = st.columns([1.5, 2], gap="medium") # Adjusted ratio for better look
        with c1:
            st.markdown(f"## Memory #{i+1}")
            st.markdown(f"#### {item['lyric']}")
            st.markdown(f"<div class='song-tag'>🎵 {item['song']}</div>", unsafe_allow_html=True)
        with c2:
            try:
                st.image(item["img"], use_container_width=True)
            except:
                st.error(f"⚠️ Image {item['img']} not found!")
    else:
        # Photo Left | Text Right
        c1, c2 = st.columns([2, 1.5], gap="medium")
        with c1:
            try:
                st.image(item["img"], use_container_width=True)
            except:
                st.error(f"⚠️ Image {item['img']} not found!")
        with c2:
            st.markdown(f"## Memory #{i+1}")
            st.markdown(f"#### {item['lyric']}")
            st.markdown(f"<div class='song-tag'>🎵 {item['song']}</div>", unsafe_allow_html=True)

    st.write("---") # Divider

# Footer
st.markdown("<h3 style='text-align: center;'>See? I told you, crazy obsessed. 🤪</h3>", unsafe_allow_html=True)