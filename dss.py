import streamlit as st
from pulp import LpMaximize, LpProblem, LpVariable
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Optimasi Rantai Pasok Agroindustri")

# Pilih antara Slider atau Number Input untuk permintaan produk
input_choice = st.selectbox("Pilih cara untuk memasukkan Permintaan Produk", ("Slider", "Input Angka"))

if input_choice == "Slider":
    # Input permintaan produk menggunakan Slider
    demand = st.slider("Masukkan Permintaan (unit)", min_value=0, max_value=100, value=50)
else:
    # Input permintaan produk menggunakan Number Input
    demand = st.number_input("Masukkan Permintaan (unit)", min_value=0, max_value=100, value=50)

input_choice = st.selectbox("Pilih cara untuk memasukkan Biaya Pengiriman per Unit", ("Slider", "Input Angka"))
if input_choice == "Slider":
    price_perunit = st.slider("Masukkan Biaya Pengiriman per Unit (Rp)", min_value=0, max_value=1000, value=200)
else:
# Input biaya pengiriman per unit (number box)
    price_perunit = st.number_input("Masukkan Biaya Pengiriman per Unit (Rp)", min_value=0, max_value=1000, value=200)

input_choice = st.selectbox("Pilih cara untuk memasukkan Kapasitas Pengiriman Maksimum", ("Slider", "Input Angka"))
if input_choice == "Slider":
    max_capacity = st.slider("Masukkan Kapasitas Pengiriman Maksimum (unit)", min_value=0, max_value=100, value=80)
else:
    max_capacity = st.number_input("Masukkan Kapasitas Pengiriman Maksimum (unit)", min_value= 0, max_value=100, value=80)
# Mendefinisikan masalah Linear Programming
model = LpProblem(name="Optimasi_Biaya_Pengiriman", sense=LpMaximize)

# Variabel keputusan: jumlah produk yang dikirim
x = LpVariable("produk_dikirim", lowBound=0, cat='Continuous')

# Fungsi objektif: meminimalkan biaya pengiriman
model += price_perunit * x  # total biaya pengiriman = biaya per unit * jumlah unit

# Kendala: permintaan produk dan kapasitas pengiriman
model += x <= demand  # Tidak bisa melebihi permintaan
model += x <= max_capacity  # Tidak bisa melebihi kapasitas pengiriman

# Menyelesaikan model
model.solve()

# Menampilkan hasil
if model.status == 1:  # Jika solusi ditemukan
    produk_dikirim = x.value()
    total_biaya = price_perunit * produk_dikirim
    st.write(f"Jumlah Produk yang Dikirim: {produk_dikirim} unit")
    st.write(f"Total Biaya Pengiriman: Rp{total_biaya}")
    
else:
    st.write("Tidak ada solusi optimal.")
