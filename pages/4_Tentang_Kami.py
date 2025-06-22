import streamlit as st
import os

st.set_page_config(page_title="Tentang Kami", layout="wide")

# Inject CSS dari style.css
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("style.css tidak ditemukan. Pastikan file ada di folder 'assets'.")

# Tambahan CSS khusus halaman ini
st.markdown("""
<style>
    html, body {
        font-family: 'Segoe UI', sans-serif;
        background-color: #ffffff;
        color: #333333;
    }
    h1, h2, h3 {
        font-weight: 700;
        margin-top: 0;
    }
    .highlight {
        color: #f47c3c;
        font-weight: bold;
    }
    .desc-text {
        font-size: 18px;
        line-height: 1.6;
        color: #555;
    }
    .rounded-image {
        border-radius: 50%;
        width: 250px;
        height: 250px;
        object-fit: cover;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# Logo kiri atas
col_logo, _ = st.columns([1, 5])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=150)
    else:
        st.warning("Logo tidak ditemukan.")

# Judul halaman
st.markdown("<h1 style='text-align: center;'>🎓 Tentang Kami</h1>", unsafe_allow_html=True)
st.markdown("---")

# Konten dua kolom
col1, col2 = st.columns([1, 2])

with col1:
    img_path = os.path.join("assets", "foto_dewi.jpg")
    if os.path.exists(img_path):
        st.markdown(f"""
        <div style='text-align: center;'>
            <img src="{img_path}" class="rounded-image">
            <p style='margin-top: 10px; color: #888;'>Dewi Yuliana</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Foto Dewi tidak ditemukan.")

with col2:
    st.markdown("""
    <h2>Diformulasikan Untuk Berbagai <span class="highlight">Kebutuhan Otomatisasi</span></h2>
    <div class="desc-text">
        <p><strong>SiramKu</strong> adalah sistem monitoring penyiraman tanaman otomatis berbasis IoT.<br>
        Sistem ini dikembangkan untuk menjawab kebutuhan pertanian modern yang efisien, berbasis data, dan ramah pengguna.</p>
    </div>
    <br>
    <h2>📌 Tentang Pengembang</h2>
    <div class="desc-text">
        <ul>
            <li><strong>Nama:</strong> Dewi Yuliana</li>
            <li><strong>NIM:</strong> 1217030008</li>
            <li><strong>Program Studi:</strong> Fisika, UIN Sunan Gunung Djati Bandung</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>© 2025 SiramKu — Tugas Akhir Mahasiswa Fisika UIN Sunan Gunung Djati Bandung</p>", unsafe_allow_html=True)
