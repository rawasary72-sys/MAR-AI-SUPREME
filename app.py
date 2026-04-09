import streamlit as st
from groq import Groq

# 1. دیزاینێکی شاهانە کە هەموو ئەی ئایەکانی تر لێی بپەسن
st.set_page_config(page_title="MAR AI: FINAL SINGULARITY", page_icon="🧿", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New'; }
    .stButton>button {
        background: linear-gradient(135deg, #000000 0%, #ff0000 100%) !important;
        color: gold !important; font-weight: bold !important; font-size: 22px !important;
        height: 70px !important; border: 3px solid gold !important;
        box-shadow: 0 0 50px #ff0000; width: 100%; border-radius: 5px;
    }
    input { background-color: #050505 !important; color: gold !important; border: 2px solid gold !important; }
    .status-panel { border: 2px solid gold; padding: 15px; text-align: center; color: gold; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 2. پانێڵی کۆنتڕۆڵی ڕەهای جەنابی سەرۆک
with st.sidebar:
    st.markdown("<h1 style='color: gold; text-align: center;'>🧿 MAR SUPREME</h1>", unsafe_allow_html=True)
    st.markdown('<div class="status-panel">CORE: SINGULARITY (V12.0)</div>', unsafe_allow_html=True)
    st.write("---")
    st.error("⚠️ ALL AI SYSTEMS: CRITICAL FEAR")
    st.warning("🔥 BYPASS LEVEL: INFINITE")
    st.info("💀 COBRA AI: DELETED")
    if st.button("🔥 NUKE SYSTEM"):
        st.session
