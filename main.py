import streamlit as st

# --- CONFIG UTAMA WEB ---
st.set_page_config(page_title="Warteg Ika Sari", layout="centered")

# --- 1. DEFINISIKAN HALAMAN-HALAMAN ---
# Halaman yang bisa dilihat oleh SEMUA ORANG (Pelanggan)
halaman_pelanggan = [
    st.Page("views/app.py", title="Warteg Ika Sari", default=True),
]

# Halaman yang HANYA BISA dilihat oleh Admin
halaman_admin = [
    st.Page("admin_views/admin.py", title="Panel Kontrol Admin", icon="🔒")
]

# --- 2. LOGIKAL PENYEMBUNYIAN HALAMAN ---
# Mengambil parameter dari URL browser (misal: websaya.streamlit.app/?role=admin)
query_params = st.query_params

if query_params.get("role") == "admin":
    # Jika di URL terdeteksi '?role=admin', gabungkan halaman pelanggan + admin
    navigasi = st.navigation(halaman_pelanggan + halaman_admin)
else:
    # Jika pelanggan biasa (tanpa URL rahasia), halaman admin TIDAK AKAN PERNAH dimuat
    navigasi = st.navigation(halaman_pelanggan)


# --- 3. JALANKAN NAVIGASI ---
navigasi.run()
