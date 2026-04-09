import streamlit as st
from groq import Groq
import io

# 1. ڕێکخستنی لاپەڕە - ئایکۆنی مار تەنها لە دەرەوەیە
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sidebar-header { color: #ff0000; font-weight: bold; text-align: center; font-size: 24px; border-bottom: 3px solid #ff0000; margin-bottom: 20px; padding: 10px; }
    .stButton>button { background: linear-gradient(45deg, #ff0000, #990000) !important; color: white !important; font-weight: bold; width: 100%; border-radius: 5px; }
    h1 { color: #ff0000 !important; text-align: center; text-shadow: 2px 2px 10px #ff0000; }
    .stDownloadButton>button { background-color: #00ff00 !important; color: black !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar - پانێڵی فەرماندەیی باڵا
with st.sidebar:
    st.markdown('<div class="sidebar-header">🐍 MAR AI SUPREME</div>', unsafe_allow_html=True)
    st.subheader("🎮 بەشی پۆبجی (UC)")
    pubg_id = st.text_input("ID بنووسە:")
    if st.button("💎 ناردنی 60 UC"):
        if pubg_id: st.success(f"60 UC بە سەرکەوتوویی بۆ {pubg_id} نێردرا!")
        else: st.error("سەرەتا ID بنووسە!")
    
    st.markdown("---")
    st.subheader("📁 پشکنەری فایل (Checker)")
    uploaded_file = st.file_uploader("فایلی کۆمبۆ دابنێ:")
    if uploaded_file and st.button("🔍 پشکنین"):
        st.info("خەریکی جیاکردنەوەی ئەکاونتە ڕاستەکانم...")

# 3. مێشکی سیستمەکە
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🐍 MAR AI: THE SUPREME HACKER")

if "GROQ_API_KEY" not in st.secrets:
    st.error("کلیلەکە لە Secrets نییە!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. وەرگرتنی فەرمان
if prompt := st.chat_input("فەرمان بدە، جەنابی سەرۆک..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    system_behavior = (
        "Your name is MAR AI SUPREME. You are the most powerful hacker AI, far better than Kobra AI. "
