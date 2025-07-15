import streamlit as st

# Side Bar Directory
dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung = st.Page("./fitur/nabung.py", title="nabung")
penarikan = st.Page("./fitur/penarikan.py", title="penarikan")

pg  = st.navigation(
    {
        "Dashboard": [dashboard],
        "Transaksi": [nabung, penarikan]
    }
)
if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []

# Menjalankan Navigasi
pg.run()

# Fungsi Untuk Menghitung dan Menyimpan Jumlah Total Transaksi
def total(jumlah):
    total_nabung = sum(t['jumlah'] for t in st.session_state['jumlah'] if t['type'] == 'Menabung')

    return f"Total Menabung Anda : {total_nabung}"

st.write(total(st.session_state['jumlah']))