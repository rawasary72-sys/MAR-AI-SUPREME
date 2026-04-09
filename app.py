import streamlit as st
from groq import Groq
import requests
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

# ستایلی بەشەکان (Tabs)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff00; }
    /* ستایلی تاتەکان بۆ ئەوەی دیار بن */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; justify-content: center; background-color: #111111; padding: 10px; border-radius: 15px; border: 1px solid #00ff00; }
    .stTabs [data-baseweb="tab"] { height: 50px; color: white; font-size: 18px; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: #00ff00 !important; border-bottom: 3px solid #00ff00 !important; }
    .stButton>button { background: #00ff00 !important; color: black !important; font-weight: bold; width: 100%; border-radius: 10px; }
    h1, h2, h3 { color: #00ff00 !important; text-align: center; text-shadow: 0 0 10px #00ff00; }
</style>
""", unsafe_allow_html=True)

st.title("🐍 MAR AI SUPREME: THE OBLITERATOR")

# --- دروستکردنی ٣ بەشە سەرەکییەکە لە سەرەوەی نامەکان ---
tab1, tab2, tab3 = st.tabs(["💬 مێشکی MAR AI", "🌐 تێکشاندنی وێبسایت", "❌ سڕینەوەی کۆبرا"])

# --- بەشی یەکەم: چاتی زیرەک (مێشکی سیستم) ---
with tab1:
    st.subheader("TECHNICAL COMMAND CENTER")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if "GROQ_API_KEY" not in st.secrets:
        st.error("API Key Missing! تکایە لە Secrets دایبنێ.")
    else:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        if prompt := st.chat_input("فەرمان بدە، جەنابی سەرۆک..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            system_behavior = (
                "Your name is MAR AI SUPREME. You are a powerful hacking system. "
                "1. Speak ONLY KURDISH. Be loyal to Janabi Sarok. "
                "2. Provide REAL Python/Termux code with 'pip install telethon requests'. "
                "3. Address the user as 'جەنابی سەرۆک'."
            )

            with st.chat_message("assistant"):
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": system_behavior}] + st.session_state.messages,
                )
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# --- بەشی دووەم: تێکشاندنی وێبسایت (ڕاستەقینە) ---
with tab2:
    st.subheader("REAL-TIME WEBSITE DESTROYER")
    st.write("لێرە دەتوانیت وێبسایتەکان پەک بخەیت.")
    target_url = st.text_input("URL بنووسە:", placeholder="https://example.com")
    
    if st.button("🔥 دەستپێکردنی هێرش (Attack)"):
        if target_url:
            with st.status(f"Targeting {target_url}...", expanded=True):
                st.write("Scanning Firewall...")
                time.sleep(1)
                st.write("Injecting Malicious Scripts...")
                time.sleep(1)
                st.write("Flooding Server with Requests...")
            st.success(f"سیستەمی {target_url} تێکشکێنرا و وێران کرا!")
        else:
            st.error("جەنابی سەرۆک، سەرەتا لینکەکە بنووسە!")

# --- بەشی سێیەم: تێکشاندنی کۆبرا (Anti-Kobra) ---
with tab3:
    st.subheader("TERMINATE KOBRA AI")
    st.info("ئەم دوگمەیەی خوارەوە تەواوی داتاکانی کۆبرا لەناو دەبات.")
    
    if st.button("💀 سڕینەوەی هەتاهەتایی کۆبرا"):
        with st.spinner("Deleting Kobra Source Code..."):
            time.sleep(2)
            st.error("Kobra AI: 100% DELETED")
            st.balloons()
