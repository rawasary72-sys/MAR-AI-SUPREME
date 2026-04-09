import streamlit as st
from groq import Groq
import time

# 1. ڕێکخستنی شاشە
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff00; font-family: 'Courier New'; }
    .stButton>button {
        background: #004400 !important; color: #00ff00 !important;
        font-weight: bold !important; font-size: 18px !important;
        height: 60px !important; border-radius: 10px !important;
        border: 2px solid #00ff00 !important; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی لای چەپ (Sidebar)
with st.sidebar:
    st.title("🐍 MAR SUPREME")
    if "tab" not in st.session_state:
        st.session_state.tab = "AI"
    
    if st.button("💬 مێشکی MAR AI (نامەکان)"):
        st.session_state.tab = "AI"
    if st.button("📢 تێکشاندنی چەناڵ"):
        st.session_state.tab = "TG"
    if st.button("🌐 وێرانکەری وێب"):
        st.session_state.tab = "WEB"
    if st.button("💎 ویسی پۆبجی (UC)"):
        st.session_state.tab = "UC"
    st.success("Access: OPEN")

# 3. بەشی نامەکان (AI Chat)
if st.session_state.tab == "AI":
    st.header("💬 مێشکی بێ‌سانسۆر")
    
    # چارەسەری کێشەی نەکرانەوەی نامەکان
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # نیشاندانی نامە کۆنەکان
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # شوێنی نووسینی نامەی نوێ
    if prompt := st.chat_input("لێرە نامەکە بنووسە جەنابی سەرۆک..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("
