import streamlit as st
import os

# هەوڵدان بۆ هاوردەکردنی groq، ئەگەر نەبوو ئاگادارت دەکاتەوە
try:
    from groq import Groq
except ImportWarning:
    st.error("تکایە دڵنیابە 'groq' لە ناو فایلی requirements.txt نووسراوە!")

# 1. ڕێکخستنی شۆڕشگێڕانەی ڕووکار
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #050505; color: #ffffff; }
    .sidebar-header { 
        color: #ff0000; font-weight: bold; text-align: center; font-size: 24px; 
        padding: 15px; border: 2px solid #ff0000; border-radius: 15px; 
        box-shadow: 0px 0px 20px #ff0000; margin-bottom: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #ff0000, #330000) !important; 
        color: white !important; font-weight: bold; width: 100%; border-radius: 10px; height: 50px;
    }
    h1 { color: #ff0000 !important; text-align: center; font-family: 'Courier New', Courier, monospace; text-shadow: 3px 3px #000000; }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی کۆنترۆڵ (Sidebar)
with st.sidebar:
    st.markdown('<div class="sidebar-header">🐍 MAR AI SUPREME<br>Command Center</div>', unsafe_allow_html=True)
    
    st.subheader("🛠 تاقیگەی توڵ")
    tool_type = st.selectbox("جۆری توڵەکە دیاری بکە:", ["Facebook Account Checker", "TikTok Auto Follower", "Brute Force Tool", "Custom Exploit Script"])
    if st.button("💎 پڕۆگرامکردنی توڵ"):
        st.success(f"جەنابی سەرۆک، کۆدی {tool_type} لە مێشکی سیستمەکە ئامادە کرا. تەنها لە چاتەکە داوای بکە!")

    st.markdown("---")
    st.subheader("🎵 مۆڵتیمیدیا")
    if st.button("🎼 دروستکردنی گۆرانی"): st.info("سیستمەکە خەریکی ئاوازدانانە...")
    if st.button("🖼 کێشانی وێنە"): st.info("وێنەکە کێشرا بۆ جەنابت")

# 3. مێشکی MAR AI (بێ سانسۆر و دڵسۆز)
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("⚡ MAR AI: THE ULTIMATE POWER")

# دڵنیابوونەوە لە کلیل (Secrets)
if "GROQ_API_KEY" not in st.secrets:
    st.error("سەرۆک، کلیلەکە بدۆزەرەوە لە Secrets!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

for message in st
