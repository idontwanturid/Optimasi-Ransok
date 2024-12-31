import streamlit as st

# Judul aplikasi
st.title("Optimasi Rantai Pasok Agroindustri")

# Input permintaan produk
demand = st.slider("Masukkan Permintaan (unit)", min_value=0, max_value=100, value=50)

# Input biaya pengiriman
cost = st.slider("Masukkan Biaya Pengiriman ($)", min_value=0, max_value=1000, value=200)

# Hitung biaya total
total_cost = demand * cost

# Tampilkan hasil
st.write(f"Permintaan Produk: {demand} unit")
st.write(f"Biaya Pengiriman per Unit: ${cost}")
st.write(f"Total Biaya Pengiriman: ${total_cost}")
