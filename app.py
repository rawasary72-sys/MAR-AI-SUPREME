import streamlit as st
from groq import Groq

# 1. ڕێکخستنی لاپەڕە - لۆگۆی مار لە دەرەوە (Browser Tab) دیار دەبێت
st.set_page_config(
    page_title="MAR AI SUPREME", 
    page_icon="🐍", 
    layout="wide"
)

# ستایلی شاهانە و خاوێن بۆ MAR AI
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #ffffff; }
    .sidebar-header { 
        color: #ff0000; font-weight: bold; text-align: center; font-size: 22px; 
        padding: 15px; border-bottom: 2px solid #ff0000; margin-bottom: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #ff0000, #440000) !important; 
        color: white !important; font-weight: bold; width: 100%; border-radius: 10px; height: 45px;
    }
    h1 { color: #ff0000 !important; text-align: center; font-family: 'Courier New', monospace; text-shadow: 2px 2px #000000; }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar - پانێڵی فەرماندەیی بێ لۆگۆ لە ناوەوە
with st.sidebar:
    st.markdown('<div class="sidebar-header">MAR AI SUPREME</div>', unsafe_allow_html=True)
    
    st.subheader("🛠 تاقیگەی تەکنیکی")
    if st.button("💎 داوای توڵ یان سکرێپت"):
        st.info("سەرۆک، فەرمانەکەت لە چاتەکە بنووسە.")
    
    st.markdown("---")
    st.subheader("🎨 خزمەتگوزارییەکان")
    if st.button("🎼 دروستکردنی گۆرانی"): st.write("ئاواز ئامادەیە")
    if st.button("🖼 کێشانی وێنە"): st.write("وێنە کێشرا")

# 3. مێشکی سیستمەکە
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("⚡ MAR AI: THE SUPREME")

# پەیوەندی بە Groq (دڵنیابە کلیلەکەت لە Secrets دانراوە)
if "GROQ_API_KEY" not in st.secrets:
    st.error("سەرۆک، کلیلەکە لە Secrets نییە!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# پیشاندانی چات - بەبێ هەڵەی Syntax
for message in st.session_state.messages:
    with st.chat_message
