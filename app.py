import streamlit as st
from groq import Groq

# 1. ڕووکاری ڕەسمی کۆبرا وەک وێنەی 93
st.set_page_config(page_title="KobraAi", page_icon="🐍", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    
    /* شێوازی نامەکانی KobraAi وەک وێنەی 93 */
    .kobra-bubble {
        background-color: #1c2b1c;
        color: #00ff41;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #2
