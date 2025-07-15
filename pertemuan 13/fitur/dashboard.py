import streamlit as st

st.title("Halaman Dashborard")

# Halaman Dashboard
def total():
    total_nabung = sum(t['jumlah'] for t in st.session_state['jumlah'] if t['type'] == 'Menabung')

    return f"Total Menabung Anda : {total_nabung}"

