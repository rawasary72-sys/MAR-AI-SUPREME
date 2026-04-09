import streamlit as st
from groq import Groq

# 1. ڕێکخستنی لاپەڕە و لۆگۆی نوێی MAR AI
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #050505; color: #ffffff; }
    /* لۆگۆی مار لە سەرەوەی لای چەپ */
    .logo-container { text-align: center; padding: 10px; }
    .logo-text { font-size: 50px; filter: drop-shadow(0px 0px 10px #ff0000); }
    
    .sidebar-header { 
        color: #ff0000; font-weight: bold; text-align: center; font-size: 20px; 
        padding: 15px; border: 2px solid #ff0000; border-radius: 15px; 
        box-shadow: 0px 0px 15px #ff0000; margin-bottom: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #ff0000, #440000) !important; 
        color: white !important; font-weight: bold; width: 100%; border-radius: 10px; height: 45px;
    }
    h1 { color: #ff0000 !important; text-align: center; font-family: 'Courier New', monospace; text-shadow: 3px 3px #000000; }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar - پانێڵی فەرماندەیی لۆگۆدار
with st.sidebar:
    st.markdown('<div class="logo-container"><span class="logo-text">🐍</span></div>', unsafe_allow_html=True)
    st.markdown
