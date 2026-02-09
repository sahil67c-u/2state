import streamlit as st
import time

# 1. Page Config
st.set_page_config(page_title="Love Coupons 🎟️", page_icon="🎁", layout="centered", initial_sidebar_state="collapsed")

# 2. THEME & CSS
st.markdown("""
    <style>
    /* Hide Sidebar */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Pink Background */
    .stApp {
        background-color: #ffe6e6;
    }
    
    /* Text Styling */
    h1, h2, h3, h4, p, div, span {
        color: #4a0010 !important; 
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: 800 !important;
    }

    /* Navigation Buttons */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white !important;
        border-radius: 10px;
        border: 2px solid #330000;
        font-weight: bold;
    }

    /* COUPON STYLE */
    .coupon-card {
        background-color: white;
        border: 2px dashed #ff4b4b;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 5px 5px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOP NAVIGATION (One Line)
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

# ================= PAGE CONTENT =================

st.title("🎁 Your Gift Coupons")
st.markdown("### Rules: You can redeem these anytime! (Terms and Conditions apply 😜)")

# Initialize Session State for Coupons
if 'redeemed' not in st.session_state:
    st.session_state.redeemed = []

# DATA: List of Coupons
# You can change these texts to whatever you want!
coupons = [
    {"id": 1, "title": "🍕 One Free Pizza Date", "desc": "I pay, you eat. No questions asked."},
    {"id": 2, "title": "💆‍♂️ Head Massage", "desc": "Valid for 15 minutes of peace."},
    {"id": 3, "title": "🤐 I Win The Argument", "desc": "Use this card to instantly win any fight."},
    {"id": 4, "title": "🎬 Movie Night Pick", "desc": "You choose the movie, I won't complain."},
    {"id": 5, "title": "🥺 Forgiveness Card", "desc": "Redeem this if you mess up big time."}
]

for coupon in coupons:
    # Check if already redeemed
    is_redeemed = coupon['id'] in st.session_state.redeemed
    
    # CSS Container for the card
    st.markdown(f"""
    <div class="coupon-card">
        <h2>{coupon['title']}</h2>
        <p>{coupon['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Button Logic
    if is_redeemed:
        st.button(f"✅ REDEEMED (#{coupon['id']})", disabled=True, key=f"btn_{coupon['id']}")
    else:
        if st.button(f"👉 Redeem This Coupon (#{coupon['id']})", key=f"btn_{coupon['id']}"):
            st.session_state.redeemed.append(coupon['id'])
            st.balloons()
            st.rerun()

    st.write("") # Spacer

if len(st.session_state.redeemed) == len(coupons):
    st.success("Woah! You used all your coupons! You are a demanding Valentine! 😂")