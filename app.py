import streamlit as st
from groq import Groq

# 1. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="MAR AI SUPREME", page_icon="⚡", layout="wide")

# 2. ستایلی Cyber و سپۆنسەر لە ناو Sidebar
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sidebar-sponsor { color: #ff0000; font-weight: bold; text-align: center; font-size: 18px; padding: 10px; border: 1px solid #ff0000; border-radius: 5px; margin-bottom: 20px; }
    .instruction-box { background-color: #1a1a1a; padding: 10px; border-radius: 5px; border-left: 5px solid #ff0000; font-size: 14px; margin-top: 20px; color: #ffffff; }
    .stButton>button { background-color: #ff0000 !important; color: white !important; font-weight: bold; width: 100%; border: none; }
    .stSelect
