import streamlit as st
import base64
import os
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model
from QAWithPDF.embedding import download_gemini_embedding, load_existing_index

# ----------------- CONFIG -----------------
st.set_page_config(page_title="AskLearn", layout="wide", page_icon="🤖")

# Particle & UFO Background
st.markdown("""
<style>
body {
    background-color: black;
    color: white;
}
canvas.particles-js-canvas-el {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
}
</style>
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
particlesJS("particles-js", {
  "particles": {
    "number": {"value": 60},
    "size": {"value": 2},
    "move": {"speed": 1},
    "line_linked": {"enable": false},
    "color": {"value": "#00FFFF"},
    "shape": {"type": "circle"}
  }
});
</script>
<div id="particles-js"></div>
""", unsafe_allow_html=True)

# ----------------- UTILS -----------------
def load_image_base64(img_path):
    try:
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

VLADIMIR_AVATAR = load_image_base64("vladimir_avatar.png")

# ----------------- SIDEBAR TOGGLE -----------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

toggle_btn = st.button("📂 Toggle Upload Panel")
if toggle_btn:
    st.session_state.sidebar_open = not st.session_state.sidebar_open

if st.session_state.sidebar_open:
    with st.sidebar:
        st.header("📂 Upload Your PDF")
        uploaded_file = st.file_uploader("Browse and upload", type=["pdf"])
        if uploaded_file:
            docs = load_data(uploaded_file)
            model = load_model()
            st.session_state.query_engine = download_gemini_embedding(model, docs)
            st.success("✅ Document embedded! You can now chat with Vladimir.")

# ----------------- CHAT -----------------
st.title("💬 Chat with Vladimir")

if "query_engine" not in st.session_state:
    st.warning("Please upload a PDF first to start chatting.")
else:
    user_input = st.text_input("Ask your question...")
    if user_input:
        response = st.session_state.query_engine.query(user_input)
        st.markdown(f"""
        <div style="display:flex; align-items:center; margin-bottom:10px;">
            {'<img src="data:image/png;base64,'+VLADIMIR_AVATAR+'" width="50">' if VLADIMIR_AVATAR else ''}
            <div style="margin-left:10px; background:#222; padding:10px; border-radius:10px;">
                {response.response}
            </div>
        </div>
        """, unsafe_allow_html=True)
