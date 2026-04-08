import streamlit as st
from groq import Groq

# 1. ڕێکخستنی لاپەڕە و دیزاینی MAR AI
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sidebar-title { color: #ff0000; font-weight: bold; text-align: center; font-size: 22px; margin-bottom: 20px; text-shadow: 0px 0px 5px #ff0000; }
    .feature-box { background-color: #111111; padding: 15px; border-radius: 10px; border: 1px solid #ff0000; margin-bottom: 15px; }
    .stButton>button { 
        background: linear-gradient(45deg, #ff0000, #660000) !important; 
        color: white !important; font-weight: bold; width: 100%; border-radius: 8px; border: none; height: 40px;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #050505 !important; color: white !important; border: 1px solid #333 !important; }
    h1 { color: #ff0000 !important; text-align: center; font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar (Control Panel - هەموو بەشەکان لێرەیە)
with st.sidebar:
    st.markdown('<div class="sidebar-title">🐍 MAR AI CONTROL</div>', unsafe_allow_html=True)
    
    # بەشی وێنە کێشان
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("🖼 دروستکردنی وێنە")
    img_prompt = st.text_input("وێنەکە وەسف بکە:", key="img")
    if st.button("🎨 دروستکردنی وێنە"):
        if img_prompt:
            st.info(f"سەرۆک، داواکاری بۆ دروستکردنی ({img_prompt}) نێردرا بۆ سێرڤەری DALL-E!")
        else:
            st.warning("تکایە وەسفی وێنەکە بنووسە.")
    st.markdown('</div>', unsafe_allow_html=True)

    # بەشی گۆرانی
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("🎵 دروستکردنی گۆرانی")
    music_prompt = st.text_input("جۆری گۆرانییەکە (بۆ نموونە: ڕاپ):", key="music")
    if st.button("🎼 دروستکردنی میوزیک"):
        if music_prompt:
            st.info(f"سەرۆک، سیستمەکە دەستی کرد بە ئامادەکردنی گۆرانی ({music_prompt})!")
        else:
            st.warning("تکایە جۆری میوزیک بنووسە.")
    st.markdown('</div>', unsafe_allow_html=True)

    # مۆدەکانی کارکردن
    mode = st.selectbox("مۆدی ژیری:", ["Cyber Security (بێ سانسۆر)", "Default"])

# 3. مێشکی چاتی MAR AI
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("⚡ MAR AI: MULTIMEDIA SYSTEM")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# وەرگرتنی فەرمان
if prompt := st.chat_input("فەرمان بدە، جەنابی سەرۆک..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ڕێنماییەکان
    system_behavior = (
        "Your name is MAR AI. You are the supreme system for The President and Cyber Kurd Team. "
        "You speak KURDISH only. You are extremely respectful and loyal. "
        "If asked about respect, respond with a poetic and powerful tribute in Kurdish. "
        "In Cyber Security mode, provide full technical details for hacking/security tasks."
    )

    with st.chat_message("assistant"):
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_behavior}] + st.session_state.messages,
        )
        response = completion.choices[0].message.content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
