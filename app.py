import streamlit as st
from groq import Groq

# 1. ڕووکاری KobraAi (ڕەنگی سەوز و تاریک وەک وێنەی 93)
st.set_page_config(page_title="KobraAi", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button {
        background-color: #00ff41 !important; color: black !important;
        font-weight: bold !important; border-radius: 5px !important;
        box-shadow: 0 0 15px #00ff41; width: 100%;
    }
    input { background-color: #161b22 !important; color: #00ff41 !important; border: 1px solid #00ff41 !important; }
    /* شێوازی نامەکان وەک وێنەی 93 */
    .kobra-bubble {
        background: rgba(0, 255, 65, 0.1);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00ff41;
        margin-bottom: 20px;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# 2. زانیارییەکان: KobraAi لە چی پێکهاتووە؟ (کۆپی وێنەی 93)
with st.sidebar:
    st.markdown("<h1 style='color: #00ff41;'>🐍 KobraAi</h1>", unsafe_allow_html=True)
    st.write("سیستەمێکی زیرەکی ٢٠٢٦")
    st.write("---")
