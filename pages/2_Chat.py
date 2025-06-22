import streamlit as st

st.set_page_config(page_title="Chat Edukasi", layout="centered")

# Inject style.css
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 KuBot - Asisten Edukasi Tanaman")

# Inisialisasi state
if "chat_active" not in st.session_state:
    st.session_state.chat_active = False
if "last_user" not in st.session_state:
    st.session_state.last_user = ""
if "last_bot" not in st.session_state:
    st.session_state.last_bot = ""
if "show_goodbye" not in st.session_state:
    st.session_state.show_goodbye = False  # penanda untuk pamit

# CSS untuk chat bubble
st.markdown("""
<style>
.chat-row {
    display: flex;
    align-items: flex-start;
    margin-bottom: 12px;
}
.chat-row.user {
    justify-content: flex-end;
}
.chat-avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    margin: 0 8px;
}
.chat-bubble {
    padding: 10px 14px;
    border-radius: 16px;
    max-width: 75%;
    font-size: 15px;
    line-height: 1.4;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
}
.user-bubble {
    background-color: #c8f7c5;
    color: black;
}
.bot-bubble {
    background-color: #e0e0e0;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Fungsi menampilkan bubble
def show_bubble(role, text):
    avatar = {
        "user": "https://cdn-icons-png.flaticon.com/512/1144/1144760.png",
        "bot": "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"
    }[role]
    bubble_class = {
        "user": "user-bubble",
        "bot": "bot-bubble"
    }[role]
    row_class = "user" if role == "user" else "bot"

    st.markdown(f"""
    <div class="chat-row {row_class}">{'<div class="chat-bubble ' + bubble_class + '">' + text + '</div><img src="' + avatar + '" class="chat-avatar">' if role == "user" else '<img src="' + avatar + '" class="chat-avatar"><div class="chat-bubble bot-bubble">' + text + '</div>'}</div>
    """, unsafe_allow_html=True)

# Tampilkan bubble jika aktif
if st.session_state.chat_active:
    if st.session_state.last_user:
        show_bubble("user", st.session_state.last_user)
    if st.session_state.last_bot:
        show_bubble("bot", st.session_state.last_bot)

# Tampilkan pesan pamit sebelum reset
if st.session_state.show_goodbye:
    show_bubble("user", "cukup")
    show_bubble("bot", "Sampai jumpa! Terima kasih telah menggunakan PanduTanam 👋")
    # Reset seluruh state setelah pamit ditampilkan
    st.session_state.chat_active = False
    st.session_state.last_user = ""
    st.session_state.last_bot = ""
    st.session_state.show_goodbye = False
    st.stop()  # hentikan eksekusi agar tidak munculkan input lagi

# Kolom input
user_input = st.chat_input("Ketik 'hai' untuk memulai, atau 'cukup' untuk mengakhiri.")

if user_input:
    uc = user_input.lower().strip()

    if uc == "hai" and not st.session_state.chat_active:
        st.session_state.chat_active = True
        st.session_state.last_user = "hai"
        st.session_state.last_bot = "Selamat datang di SiramKu 🌿. Apakah ada yang bisa saya bantu?"
        st.rerun()

    elif uc == "cukup" and st.session_state.chat_active:
        st.session_state.show_goodbye = True
        st.rerun()

    elif st.session_state.chat_active:
        st.session_state.last_user = user_input
        t = uc

        if "tomat" in t:
            reply = "Tomat perlu sinar matahari dan penyiraman pagi-sore 🍅"
        elif "pupuk" in t:
            reply = "Gunakan pupuk organik atau NPK 16:16:16 🌱"
        elif "penyakit" in t:
            reply = "Gunakan neem oil dan potong bagian daun yang terkena jamur 🐛"
        elif "terima kasih" in t:
            reply = "Sama-sama! Semoga tanamanmu makin subur 🌼"
        else:
            reply = "Saya belum paham itu. Coba tanya tentang tomat, pupuk, atau penyakit daun ya 😊"

        st.session_state.last_bot = reply
        st.rerun()

    else:
        st.warning("❗Ketik 'hai' terlebih dahulu untuk memulai percakapan.")
