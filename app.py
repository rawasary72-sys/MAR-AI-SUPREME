import streamlit as st
from groq import Groq

# 1. ڕێکخستنی لاپەڕە و ستایلی مار ئەی ئای
st.set_page_config(page_title="MAR AI SUPREME", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sidebar-sponsor { 
        color: #ff0000; font-weight: bold; text-align: center; font-size: 18px; 
        padding: 15px; border: 2px solid #ff0000; border-radius: 12px; 
        margin-bottom: 20px; background-color: #0a0a0a; box-shadow: 0px 0px 10px #ff0000;
    }
    .tiktok-section { background-color: #1
