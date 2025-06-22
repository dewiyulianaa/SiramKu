import streamlit as st

st.set_page_config(page_title="Edukasi", layout="wide")

# Inject style.css
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Inject custom CSS tambahan untuk halaman ini
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #333;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #27ae60;
        color: #ecf0f1;
    }
    </style>
""", unsafe_allow_html=True)

st.title("\U0001F4DA Edukasi Tanaman")
st.markdown("Dapatkan informasi penting terkait budidaya, penyakit, dan perawatan tanaman.")
st.markdown("---")

# Layout 3 kolom seperti portal berita
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://media.istockphoto.com/id/182067740/id/foto/tomat-busuk.jpg?s=612x612&w=0&k=20&c=iCjbpBv6yjXROl1iibuTLtfJ1rkuXt82C3mH5e78gtg=", use_container_width=True)
    st.markdown("### \U0001F345 Penyakit Tomat")
    st.markdown("Pelajari cara mengatasi busuk buah, layu fusarium, dan virus TYLCV pada tomat.")
    st.link_button("Baca Selengkapnya", "https://www.dgwfertilizer.co.id/3-penyakit-tanaman-tomat-serta-cara-mengendalikannya/")

with col2:
    st.image("https://www.dgwfertilizer.co.id/wp-content/uploads/2020/10/Pupuk-NPK-GOLD-DGW-Pupuk-HX-DAP-768x515.jpg", use_container_width=True)
    st.markdown("### \U0001F33E Pupuk Tanaman")
    st.markdown("Kenali jenis pupuk terbaik untuk menunjang pertumbuhan tanaman sehat dan produktif.")
    st.link_button("Pelajari Lebih Lanjut", "https://nufarm.com/id/penyakit-busuk-buah-tomat/")

with col3:
    st.image("https://img.youtube.com/vi/xxJhFXNpa60/0.jpg", use_container_width=True)
    st.markdown("### \U0001F3A5 Video Edukasi Tomat")
    st.markdown("Simak video budidaya tomat di polybag, mulai dari penanaman hingga panen.")
    st.link_button("Tonton Video", "https://youtu.be/xxJhFXNpa60?si=V_8UyLzWJjGvoEKn")

st.markdown("---")

# Footer info
st.info("\U0001F516 Konten ini dikurasi dari sumber terpercaya seperti Kementerian Pertanian dan video edukatif YouTube.")
