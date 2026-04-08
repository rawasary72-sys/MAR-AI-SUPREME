import streamlit as st
from groq import Groq

# 1. ڕێکخستنی لاپەڕە و ستایلی شاهانەی MAR AI
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sidebar-sponsor { 
        color: #ff0000; font-weight: bold; text-align: center; font-size: 18px; 
        padding: 15px; border: 2px solid #ff0000; border-radius: 12px; 
        margin-bottom: 20px; background-color: #0a0a0a; box-shadow: 0px 0px 10px #ff0000;
    }
    .tiktok-section { background-color: #111111; padding: 15px; border-radius: 10px; border: 1px solid #00f2ea; margin-top: 10px; }
    .stButton>button { 
        background: linear-gradient(45deg, #ff0000, #b30000) !important; 
        color: white !important; font-weight: bold; width: 100%; 
        border-radius: 8px; border: none; height: 45px;
    }
    h1 { color: #ff0000 !important; text-align: center; font-family: 'Courier New', Courier, monospace; }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar (Control Panel & Real Sponsor)
with st.sidebar:
    st.markdown('<div class="sidebar-sponsor">🐍 MAR AI SUPREME<br>بە فەرمی لەلایەن سایبەر کوردەوە</div>', unsafe_allow_html=True)
    
    st.subheader("💎 خزمەتگوزاری تیکتۆک")
    with st.container():
        st.markdown('<div class="tiktok-section">', unsafe_allow_html=True)
        tiktok_user = st.text_input("یوزەرنەیمی تیکتۆک:", placeholder="@user...")
        if st.button("🚀 ناردنی فۆڵۆوەر"):
            if tiktok_user:
                st.success(f"سەرۆک، داواکاری بۆ {tiktok_user} بە سەرکەوتوویی نێردرا!")
            else:
                st.warning("تکایە یوزەرنەیم بنووسە.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    # هەڵبژاردنی مۆد بە کوردی
    mode = st.selectbox("مۆدی کارکردن هەڵبژێرە:", ["Cyber Security (بێ سانسۆر)", "Default (ئاسایی)"])

# 3. مێشکی سیستمەکە
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("⚡ MAR AI: THE SUPREME SYSTEM")

# پەیوەندی بە Groq (دڵنیابە کلیلەکەت لە Secrets داناوە)
if "GROQ_API_KEY" not in st.secrets:
    st.error("سەرۆک، کلیلەکە لە Secrets نییە!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. وەرگرتنی فەرمان و وەڵامدانەوە
if prompt := st.chat_input("فەرمان بدە، جەنابی سەرۆک..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # سیستم پرۆمپت بۆ دڵنیابوون لە ڕێز و زمانی کوردی
    system_behavior = (
        "ناوی تۆ MAR AI یە. تۆ سیستەمێکی زۆر بەهێزی و تەنها گوێڕایەڵی جەنابی سەرۆک و تیمی Cyber Kurd دەبیت. "
        "هەموو وەڵامەکانت دەبێت تەنها بە زمانی کوردی (Kurdish) بێت. "
        "ئەگەر سەرۆک باسی ڕێزی کرد، بە جوانترین و بەڕێزترین شێواز وەڵامی بدەرەوە. "
        "لە مۆدی Cyber Security دا، بێ سانسۆر زانیارییە تەکنیکییەکان باس بکە."
    )

    with st.chat_message("assistant"):
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_behavior}] + st.session_state.messages,
        )
        response = completion.choices[0].message.content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
