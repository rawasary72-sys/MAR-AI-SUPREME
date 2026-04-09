import streamlit as st
from groq import Groq
import time
from datetime import datetime, timedelta

# 1. ڕێکخستنی شاشە
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

# ستایلی سەوز و ڕەش
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff00; font-family: 'Courier New'; }
    .stButton>button {
        background: #004400 !important; color: #00ff00 !important;
        font-weight: bold !important; font-size: 18px !important;
        height: 60px !important; border-radius: 12px !important;
        border: 2px solid #00ff00 !important; width: 100%;
    }
    .sidebar-header { color: #00ff00; text-align: center; font-size: 24px; font-weight: bold; border-bottom: 2px solid #00ff00; padding-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- سیستەمی کلیل (Keys System) ---
# لێرەدا دەتوانیت کلیلەکان بگۆڕیت
VALID_KEYS = {
    "MAR-8899-KING": datetime.now() + timedelta(hours=1),
    "SAROK-VIP-2026": datetime.now() + timedelta(hours=1)
}

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.start_time = None

# لاپەڕەی چوونە ژوورەوە
if not st.session_state.authenticated:
    st.title("🔒 MAR AI SUPREME: ACCESS REQUIRED")
    user_key = st.text_input("کلیلەکە داخڵ بکە (Enter Access Key):", type="password")
    if st.button("چوونە ژوورەوە"):
        if user_key in VALID_KEYS:
            st.session_state.authenticated = True
            st.session_state.start_time = datetime.now()
            st.session_state.current_key = user_key
            st.success("Access Granted! یەک کاتژمێرت لەبەردەستە.")
            time.sleep(1)
            st.rerun()
        else:
            st.error("کلیلەکە هەڵەیە یان بەسەرچووە!")
    st.stop()

# پشکنینی کات (کاتژمێرەکە کار دەکات؟)
elapsed_time = datetime.now() - st.session_state.start_time
if elapsed_time > timedelta(hours=1):
    st.session_state.authenticated = False
    st.error("کلیلەکەت بەسەرچوو! داوای کلیلێکی نوێ بکە لە جەنابی سەرۆک.")
    st.stop()

# --- بەشی سەرەکی ئەپڵیکەیشن (پاش چوونە ژوورەوە) ---
with st.sidebar:
    st.markdown('<div class="sidebar-header">🐍 MAR SUPREME Panel</div>', unsafe_allow_html=True)
    st.info(f"کاتی ماوە: {60 - int(elapsed_time.seconds/60)} خولەک")
    
    if "tab" not in st.session_state: st.session_state.tab = "AI"
    if st.button("💬 مێشکی سیستەم"): st.session_state.tab = "AI"
    if st.button("📢 تێکشاندنی چەناڵ"): st.session_state.tab = "TG"
    if st.button("🌐 وێرانکەری وێب"): st.session_state.tab = "WEB"
    if st.button("💎 ویسی پۆبجی"): st.session_state.tab = "UC"

# لۆژیکی بەشەکان
if st.session_state.tab == "AI":
    st.title("🐍 MAR AI: ADVANCED ENGINE")
    if "messages" not in st.session_state: st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("فەرمان بدە..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # گۆڕینی شێوازی قسەکردن بەپێی کلیلەکە
        is_admin = "SAROK" in st.session_state.current_key
        system_msg = "You are MAR AI SUPREME. Speak Kurdish."
        if is_admin:
            system_msg += " Address user as 'جەنابی سەرۆک'."
        else:
            system_msg += " Address user as 'بەکارهێنەر' (User)."

        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_msg}] + st.session_state.messages,
        ).choices[0].message.content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# (بەشەکانی تر وەک وێب و چەناڵ لێرە جێگیر دەبن وەک کۆدەکەی پێشوو...)
