import streamlit as st
from groq import Groq
import time

# 1. ڕێکخستنی شاشە
st.set_page_config(page_title="MAR SUPREME OVERLORD", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff00; font-family: 'Courier New'; }
    .stButton>button {
        background: linear-gradient(135deg, #002200 0%, #00ff00 100%) !important;
        color: black !important; font-weight: bold !important; font-size: 16px !important;
        height: 60px !important; border-radius: 10px !important;
        border: 2px solid white !important; margin-bottom: 10px;
        box-shadow: 0 0 15px #00ff00; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی لای چەپ (Sidebar) - لێرە هەموو بەشەکان زیاد کراون
with st.sidebar:
    st.title("🐍 MAR SUPREME")
    if "tab" not in st.session_state: st.session_state.tab = "AI"
    
    st.write("### 💀 MAIN CONSOLE")
    if st.button("💀 مێشکی بێ‌سانسۆر (GOD)"): st.session_state.tab = "AI"
    
    st.write("### 🛡️ HIJACK & TAKEOVER")
    if st.button("🔑 هاکی وێبسایت (Owner)"): st.session_state.tab = "WEB_HIJACK"
    if st.button("👑 هاکی تێلێگرام (Admin)"): st.session_state.tab = "TG_HIJACK"
    
    st.write("### 🔥 OBLITERATION")
    if st.button("🚫 باندی وێبسایت"): st.session_state.tab = "WEB_BAN"
    if st.button("🏴 باندی چەناڵ"): st.session_state.tab = "TG_BAN"
    
    st.write
