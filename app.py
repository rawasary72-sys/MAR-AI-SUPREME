import streamlit as st
from groq import Groq

# 1. ڕووکاری KobraAi وەک وێنەی 93
st.set_page_config(page_title="KobraAi", page_icon="🐍", layout="centered")

st.markdown("""
<style>
    /* باکگراوندی ڕەش و تاریک */
    .stApp { background-color: #0b0f12; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* شێوازی نامەکانی KobraAi وەک وێنەی 93 */
    .kobra-msg-container {
        background-color: #1c2b1c; /* ڕەنگی سەوزی تاریک */
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #2d4a2d;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* شێوازی نامەکانی جەنابی سەرۆک */
    .user-msg-container {
        background-color: #162a3d; /* ڕەنگی شینی تاریک */
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #1f3d5a;
        margin-bottom: 15px;
        text-align: right;
    }

    .kobra-header { color: #00ff41; font-weight: bold; margin-bottom: 5px; display: flex; align-items: center; }
    .user-header { color: #3498db; font-weight: bold; margin-bottom: 5px; }

    /* دیزاینی دوگمە و ئینپوت */
    .stButton>button { background-color: #1f8b4c !important; color: white !important; border-radius: 20px !important; border: none; }
    input { background-color: #1c2
