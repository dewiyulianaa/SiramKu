import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="SiramKu", layout="centered")

# Inject style.css
with open("assets/style.css") as f:
    content = f.read()
    st.markdown(f"<style>{content}</style>", unsafe_allow_html=True)
    st.write("CSS Loaded:", len(content))  # cek panjang file, harus > 0

# Tambahan CSS kustom dark mode
st.markdown("""
<style>
body {
    background-color: #000000;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}
.big-title {
    font-size: 50px;
    font-weight: 800;
    color: #ffffff;
    text-align: center;
    margin-top: 20px;
}
.subtitle {
    font-size: 22px;
    font-weight: 400;
    text-align: center;
    color: #aaaaaa;
    margin-bottom: 40px;
    line-height: 1.6;
}
.center-button {
    display: flex;
    justify-content: center;
    margin-top: 30px;
}
.mockup {
    display: flex;
    justify-content: center;
    margin-top: 50px;
}
button[kind="primary"] {
    background-color: #ffcc00;
    color: #000;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 25px;
}
</style>
""", unsafe_allow_html=True)

# Logo di kiri atas
# Logo besar tengah halaman (hero section)
st.markdown("<div style='text-align: center; padding-top: 30px;'>", unsafe_allow_html=True)
st.image("assets/logo.png", width=180)
st.markdown("</div>", unsafe_allow_html=True)

# Konten utama
st.markdown('<div class="big-title">Hi, I’m SiramKu</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Saya membantu Anda memantau dan merawat tanaman secara otomatis\nmenggunakan teknologi IoT dan AI.</div>', unsafe_allow_html=True)

# Tombol navigasi
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌿 Mulai Pantau Tanaman"):
        st.switch_page("1_dashboard.py")


