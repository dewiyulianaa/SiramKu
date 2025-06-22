import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time

st.set_page_config(page_title="Dashboard Monitoring", layout="wide")

# Inject style.css
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📊 Dashboard Monitoring Tanaman")

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = dict(st.secrets["gspread"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)



# Ambil data dari Google Sheet
try:
    spreadsheet = client.open_by_key("19dRpsMDpz8EcSnyIYVz_fYjnz55-Id1j5SHZzzTBTnE")  # Ganti dengan ID Spreadsheet
    sheet = spreadsheet.sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    # Menampilkan data terbaru
    if not df.empty:
        latest = df.iloc[-1]
        st.success(f"📅 Data Terbaru - {latest['Waktu']}")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🌱 Kelembaban Tanah", f"{latest['Kelembaban Tanah']} %")
        with col2:
            st.metric("🌡 Suhu", f"{latest['Suhu']} °C")
        with col3:
            st.metric("💧 Kelembaban Udara", f"{latest['Kelembaban Udara']} %")
        with col4:
            st.metric("📍 Status Tanah", latest.get("Status Tanah", "N/A"))

        # Tabel dan grafik
        st.markdown("---")
        st.subheader("📋 Tabel Data Sensor")
        st.dataframe(df)

        st.subheader("📈 Grafik Kelembaban Tanah")
        st.line_chart(df["Kelembaban Tanah"])

        st.subheader("🌡️ Grafik Suhu & Kelembaban Udara")
        st.line_chart(df[["Suhu", "Kelembaban Udara"]])

        st.info("⏳ Dashboard akan diperbarui otomatis setiap 5 detik...")
        time.sleep(5)
        st.rerun()

    else:
        st.warning("⚠️ Data Google Sheet kosong atau belum tersedia.")

except Exception as e:
    st.error(f"❌ Gagal mengambil data dari Google Sheets:\n{e}")
