import streamlit as st
from groq import Groq

# 1. دیزاینی وەک کۆبرا ئەی ئای (ڕەنگی سەوز و ڕەش)
st.set_page_config(page_title="KobraAi - MAR Edition", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp {
        background-color: #050505;
        color: #00ff41; /* ڕەنگی سەوزی تێرمیناڵی کۆبرا */
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: #00ff41 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 5px !important;
        border: none !important;
        box-shadow: 0 0 15px #00ff41;
        width: 100%;
    }
    input { 
        background-color: #111 !important; 
        color: #00ff41 !important; 
        border: 1px solid #00ff41 !important; 
    }
    .kobra-msg {
        background: rgba(0, 255, 65, 0.1);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #00ff41;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 2. ڕووکاری چوونە ژوورەوە و ناسنامە
with st.sidebar:
    st.markdown("<h2 style='color: #00ff
