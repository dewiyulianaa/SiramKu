import streamlit as st
import os

st.set_page_config(page_title="SiramKu", layout="centered")

# Load CSS dari assets/style.css jika ada
css_path = os.path.join("assets", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("style.css tidak ditemukan.")

# Tambahan CSS dark mode langsung
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
    text-align: center;
    color: #ffffff;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: #cccccc;
    line-height: 1.6;
    margin-bottom: 40px;
}
.stButton button {
    background-color: #ffcc00;
    color: #000000;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 30px;
}
</style>
""", unsafe_allow_html=True)

# Logo SiramKu di tengah
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=180)
else:
    st.warning("Logo tidak ditemukan.")

# Teks utama
st.markdown('<div class="big-title">Hi, I’m SiramKu</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Saya membantu Anda memantau dan merawat tanaman secara otomatis<br>menggunakan teknologi IoT dan AI.</div>', unsafe_allow_html=True)

# Tombol Navigasi
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌿 Mulai Pantau Tanaman"):
        # INI HARUS PERSIS SAMA dengan nama file di folder pages/
        st.switch_page("pages/1_Dashboard.py")
