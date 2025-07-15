import streamlit as st

st.title("Halaman Menabung")

#Halaman Menabung
with st.form("form_nabung"):
    nama = st.text_input("Masukkan Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    submit_button = st.form_submit_button(label="Menabung")
    if submit_button:
        st.session_state['jumlah'].append({
            "type" : "Menabung",
            "nama" : nama,
            "jumlah" : jumlah
        })
        st.success("Menabung Berhasil")
    
    else:
        st.error("Gagal")