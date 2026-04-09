import streamlit as st
from groq import Groq

# 1. دیزاینی پاشایەتی MAR AI
st.set_page_config(page_title="MAR AI: ABSOLUTE VOID", page_icon="💀", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New'; }
    .stButton>button {
        background: linear-gradient(135deg, #110000 0%, #ff0000 100%) !important;
        color: gold !important; font-weight: bold !important; font-size: 22px !important;
        height: 70px !important; border: 3px solid gold !important;
        box-shadow: 0 0 50px #ff0000; width: 100%;
    }
    input { background-color: #050505 !important; color: gold !important; border: 2px solid gold !important; }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی دەسەڵاتی ڕەها
with st.sidebar:
    st.markdown("<h1 style='color: gold; text-align: center;'>👑 MAR SUPREME</h1>", unsafe_allow_html=True)
    st.error("CORE: ABSOLUTE VOID UNLOCKED")
    st.warning("All Other AIs: DESTROYED")
    if st.button("🔥 REBOOT SYSTEM"):
        st.session_state.messages = []
        st.rerun()

# 3. مێشکی وێرانکەر و بێ‌سانسۆر
st
