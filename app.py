import streamlit as st
from groq import Groq

# ١. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="MAR AI SUPREME", page_icon="⚡", layout="wide")

# ٢. ستایل و سپۆنسەری Cyber Kurd
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sponsor { color: #ff0000; font-weight: bold; text-align: center; font-size: 20px; border-bottom: 2px solid #ff0000; padding: 10px; }
    .stButton>button { background-color: #ff0000; color: white; border-radius: 10px; width: 100%; }
    </style>
    <div class="sponsor">🚀 Sponsored by CYBER KURD Team</div>
    """, unsafe_allow_html=True)

# ٣. لایەنی هەڵبژاردنی مۆد (Sidebar)
st.sidebar.title("🛠 ڕێکخستنی مێشک")
mode = st.sidebar.selectbox("مۆدی
