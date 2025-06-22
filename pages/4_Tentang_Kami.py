import streamlit as st

st.set_page_config(page_title="Tentang Kami", layout="wide")

# Inject CSS dari style.css
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
    st.image("assets/logo.png", width=180)

# Judul halaman
st.markdown("<h1 style='text-align: center;'>🎓 Tentang Kami</h1>", unsafe_allow_html=True)
st.markdown("---")

# Konten dua kolom
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/foto_dewi.jpg", width=220, caption="Dewi Yuliana", use_container_width=False)
    st.markdown("""
        <style>
        img {
            border-radius: 50%;
            object-fit: cover;
        }
        </style>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <h2>Diformulasikan Untuk Berbagai <span class="highlight">Kebutuhan Otomatisasi</span></h2>
    <div class="desc-text">
    <Sistem><strong>SiramKu</strong> adalah sistem monitoring penyiraman tanaman otomatis berbasis IoT.Sistem ini dikembangkan untuk menjawab kebutuhan pertanian modern yang efisien, berbasis data, dan ramah pengguna.</p>
    </div>
    <br>
    <h2>📌 Tentang Pengembang</h3>
    <div class="desc-text">
    <ul>
        <li><strong>Nama:</strong> Dewi Yuliana</li>
        <li><strong>NIM:</strong> 1217030008</li>
        <li><strong>Program Studi:</strong> Fisika, UIN Sunan Gunung Djati Bandung</li>
    </ul>
    </div>
    <br>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>© 2025 SiramKu — Tugas Akhir Mahasiswa Fisika UIN Sunan Gunung Djati Bandung</p>", unsafe_allow_html=True)
