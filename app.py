import streamlit as st
from groq import Groq
import time

# 1. ڕێکخستنی شاشە و دیزاینی سەربازی
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff00; font-family: 'Courier New'; }
    .stButton>button {
        background: linear-gradient(135deg, #004400 0%, #00ff00 100%) !important;
        color: black !important; font-weight: bold !important; font-size: 18px !important;
        height: 65px !important; border-radius: 10px !important;
        border: 2px solid white !important; margin-bottom: 10px;
    }
    .sidebar-header { color: #00ff00; text-align: center; font-size: 22px; font-weight: bold; border-bottom: 2px solid #00ff00; padding-bottom: 10px; }
    input { background-color: #0a0a0a !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی کۆنترۆڵی لای چەپ (بە بێ کلیل)
with st.sidebar:
    st.markdown('<div class="sidebar-header">🐍 MAR SUPREME CONTROL</div>', unsafe_allow_html=True)
    if "tab" not in st.session_state: st.session_state.tab = "AI"
    
    if st.button("💬 مێشکی بێ‌سانسۆر"): st.session_state.tab = "AI"
    if st.button("📢 تێکشاندنی چەناڵ"): st.session_state.tab = "TG"
    if st.button("🌐 وێرانکەری وێب"): st.session_state.tab = "WEB"
    if st.button("💎 ویسی پۆبجی (UC)"): st.session_state.tab = "UC"
