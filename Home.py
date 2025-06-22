import streamlit as st
import os

st.set_page_config(page_title="SiramKu", layout="centered")

# ✅ Inject CSS dari file style.css
css_path = os.path.join("assets", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        content = f.read()
        st.markdown(f"<style>{content}</style>", unsafe_allow_html=True)
else:
    st.warning("style.css tidak ditemukan.")

# ✅ Tambahan CSS khusus halaman ini (inline)
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
button[kind="primary"] {
    background-color: #ffcc00 !important;
    color: #000000 !important;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 25px;
}
</style>
""", unsafe_allow_html=True)

# ✅ Tampilkan logo di tengah atas
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.markdown("<div style='text-align: center; padding-top: 30px;'>", unsafe_allow_html=True)
    st.image(logo_path, width=180)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.error("Logo tidak ditemukan.")

# ✅ Teks hero section
st.markdown('<div class="big-title">Hi, I’m SiramKu</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Saya membantu Anda memantau dan merawat tanaman secara otomatis<br>menggunakan teknologi IoT dan AI.</div>', unsafe_allow_html=True)

# ✅ Tombol navigasi ke Dashboard
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌿 Mulai Pantau Tanaman"):
        # Pastikan file ini berada di `pages/1_Dashboard.py` (bukan 1_dashboard.py)
        st.switch_page("1_Dashboard.py")  # Nama file case-sensitive
