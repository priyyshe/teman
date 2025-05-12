import streamlit as st

st.set_page_config(page_title="siapakah dia?", page_icon=":tada:", layout="centered")
st.title("Tes Siapakah Dia? :tada:")
st.image("https://wallpapercave.com/wp/wp4348969.jpg", width=300)
st.write("Jawab beberapa pertanyaan berikut untuk mengetahui siapa dia!")

# Inisialisasi skor
score = {
    "Nazla": 0,
    "Bina": 0,
    "Sheila": 0
}

#pertanyaan 1
q1 = st.radio("1. Aktivitas favoritnya?", ["Melihat bulan", "Mendengarkan musik", "scrolling tiktok"])
if q1 == "Melihat bulan":
    score["Bina"] += 1
elif q1 == "Mendengarkan musik":
    score["Sheila"] += 1
elif q1 == "scrolling tiktok":
    score["Nazla"] += 1
    
#tombol untuk melihat hasil
if st.button("🎉 Lihat Hasil"):
    # Cek apakah semua pertanyaan dijawab
    if q1:
        hasil = max(score, key=score.get)
        st.success(f"✅ Dia adalah: **{hasil}**!")
        st.balloons()
    else:
        st.warning("⚠️ Harap jawab semua pertanyaan dulu.")
