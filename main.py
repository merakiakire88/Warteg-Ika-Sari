import streamlit as st

# --- CONFIG UTAMA WEB ---
st.set_page_config(page_title="Warteg Ika Sari", layout="centered")

# --- 1. DEFINISIKAN HALAMAN-HALAMAN ---
halaman_pelanggan = [
    st.Page("views/app.py", title="Warteg Ika Sari", default=True),
]

halaman_admin = [
    st.Page("admin_views/admin.py", title="Panel Kontrol Admin", icon="🔒")
]


# --- 2. LOGIKAL PENYEMBUNYIAN HALAMAN (PERBAIKAN) ---
# Inisialisasi status admin di session state jika belum ada
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# Ambil query parameter dari URL
query_params = st.query_params

# Cek apakah ada parameter ?role=admin di URL
if query_params.get("role") == "admin":
    st.session_state.is_admin = True
    # OPSIONAL: Hapus parameter dari URL agar URL kembali bersih setelah login sukses
    st.query_params.clear() 

# Tentukan menu navigasi berdasarkan st.session_state
if st.session_state.is_admin:
    # Jika sudah terverifikasi admin, menu admin akan terus terkunci di sidebar
    navigasi = st.navigation(halaman_pelanggan + halaman_admin)
else:
    # Jika pelanggan biasa
    navigasi = st.navigation(halaman_pelanggan)


# --- 3. JALANKAN NAVIGASI ---
navigasi.run()
