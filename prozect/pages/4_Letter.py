import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Open When... 💌", page_icon="🥺", layout="centered", initial_sidebar_state="collapsed")

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
        font-size: 14px;
        padding: 5px;
    }

    /* Letter Box Style */
    .stExpander {
        background-color: white;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        border: 2px solid #ffcccc;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOP NAVIGATION (5 Icons for space saving)
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

st.title("💌 Open When...")
st.markdown("### Click on a letter when you feel this way...")

# Letter 1
with st.expander("...you miss me 🥺"):
    st.markdown("""
    ### I miss you too! 
    Remember that distance is just a test to see how far love can travel. 
    Look at this photo and smile for me:
    """)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2QzM3Z6cW93aW55eXJ6eXJ6eXJ6eXJ6eXJ6eXJ6eXJ6eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif")
    st.write("Call me right now. I'm waiting.")

# Letter 2
with st.expander("...you are mad at me 😡"):
    st.markdown("""
    ### Okay, I'm sorry.
    I know I can be annoying sometimes (or a lot of times). 
    But I love you more than anything. 
    
    Please forgive me? 🥺
    """)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWR5amF4aGZ4aGZ4aGZ4aGZ4aGZ4aGZ4aGZ4aGZ4aGZ4aSZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/3o7TKr3nzbh5WgCFxe/giphy.gif")

# Letter 3
with st.expander("...you feel sad 😢"):
    st.markdown("""
    ### Don't be sad, sunshine! ☀️
    You have the most beautiful smile in the world. 
    Whatever is bothering you, we will fix it together.
    
    Here is a virtual hug:
    """)
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif")

# Letter 4
with st.expander("...it's our Anniversary 🎉"):
    st.markdown("""
    ### Happy Anniversary my Love! ❤️
    I can't believe another year has passed.
    You are the best thing that ever happened to me.
    
    (Put a secret code or location of a real gift here!)
    """)
    st.balloons()