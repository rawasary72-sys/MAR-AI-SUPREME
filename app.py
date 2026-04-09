import streamlit as st
from groq import Groq

# 1. دیزاینی ژووری فەرماندەیی هاکەران
st.set_page_config(page_title="MAR AI: HACKER KING", page_icon="🏴‍☠️", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff00; font-family: 'Courier New'; }
    .stButton>button {
        background: linear-gradient(135deg, #000000 0%, #00ff00 100%) !important;
        color: black !important; font-weight: bold !important; font-size: 20px !important;
        height: 60px !important; border: 2px solid white !important;
        box-shadow: 0 0 40px #00ff00; width: 100%;
    }
    input { background-color: #0a0a0a !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
    .status-panel { border: 2px solid #00ff00; padding: 10px; color: #00ff00; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی دەسەڵاتی ڕەهای ڕەوا گیان
with st.sidebar:
    st.markdown("
