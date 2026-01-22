import streamlit as st

# --- KONFIGURASI HALAMAN ---
# Mengatur judul tab browser dan ikon
st.set_page_config(
    page_title="Galeri Rally & Bus",
    page_icon="🏎️",
    layout="centered"
)

# --- DATA GAMBAR (URL) ---
# Kita gunakan dictionary untuk menyimpan URL gambar agar rapi.
# Saya menggunakan URL gambar publik dari Wikipedia sebagai contoh.
data_kendaraan = {
    "rally": {
        "Subaru Impreza WRC (Iconic Blue)": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Subaru_Impreza_WRC_2001.jpg/1024px-Subaru_Impreza_WRC_2001.jpg",
        "Toyota Yaris WRC (Modern Era)": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Toyota_Yaris_WRC_2019.jpg/1024px-Toyota_Yaris_WRC_2019.jpg",
        "Audi Quattro A2 (Group B Legend)": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Audi_Quattro_A2_at_Race_Retro_2008.jpg/1024px-Audi_Quattro_A2_at_Race_Retro_2008.jpg"
    },
    "bus": {
        "Scania Touring Coach (Bis Pariwisata)": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Scania_Touring_HD_in_Krak%C3%B3w.jpg/1024px-Scania_Touring_HD_in_Krak%C3%B3w.jpg",
        "London Double Decker (Bis Tingkat)": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/LT_471_%28LTZ_1471%29_Arriva_London_New_Routemaster_%2819522859218%29.jpg/1024px-LT_471_%28LTZ_1471%29_Arriva_London_New_Routemaster_%2819522859218%29.jpg",
        "Mercedes-Benz Citaro (Bis Kota)": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Mercedes-Benz_Citaro_G_BlueTec_Hybrid_Bus_Hannover.jpg/1024px-Mercedes-Benz_Citaro_G_BlueTec_Hybrid_Bus_Hannover.jpg"
    }
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigasi Kendaraan")
st.sidebar.write("Gunakan menu di bawah untuk memilih jenis kendaraan.")

# Ini adalah "slides bar" (selectbox) di samping untuk memilih kategori utama
kategori_pilihan = st.sidebar.selectbox(
    "Pilih Kategori Utama:",
    ("Rally Car 🏎️", "Bus 🚌")
)

st.sidebar.markdown("---")
st.sidebar.info("Aplikasi ini menampilkan galeri kendaraan berdasarkan pilihan Anda di sidebar.")


# --- KONTEN UTAMA ---
st.title("Showroom Kendaraan Virtual")

# Logika Percabangan berdasarkan pilihan Sidebar
if kategori_pilihan == "Rally Car 🏎️":
    # Header khusus Rally
    st.header("🔥 Kategori: Mobil Rally")
    st.write("Mobil-mobil ini dirancang untuk kecepatan tinggi di medan tanah, kerikil, dan aspal yang ekstrem.")
    
    # Mengambil daftar kunci (nama mobil) dari data rally
    daftar_model_rally = list(data_kendaraan["rally"].keys())
    
    # Pilihan tambahan di halaman utama untuk model spesifik
    col1, col2 = st.columns([1, 2])
    with col1:
         pilihan_model = st.selectbox("Pilih Model Rally Car:", daftar_model_rally)
    
    # Menampilkan gambar berdasarkan model yang dipilih
    url_gambar = data_kendaraan["rally"][pilihan_model]
    
    with col2:
        # use_column_width=True agar gambar menyesuaikan lebar kolom
        st.image(url_gambar, caption=f"Model: {pilihan_model}", use_column_width=True)
        st.success(f"Menampilkan: {pilihan_model}")


elif kategori_pilihan == "Bus 🚌":
    # Header khusus Bus
    st.header("🛣️ Kategori: Bis Transportasi")
    st.write("Kendaraan besar yang dirancang untuk mengangkut banyak penumpang dalam kenyamanan.")
    
    # Mengambil daftar kunci (nama bis) dari data bus
    daftar_model_bus = list(data_kendaraan["bus"].keys())
    
    # Pilihan tambahan di halaman utama untuk model spesifik
    col1, col2 = st.columns([1, 2])
    with col1:
        pilihan_model = st.selectbox("Pilih Model Bis:", daftar_model_bus)
        
    # Menampilkan gambar berdasarkan model yang dipilih
    url_gambar = data_kendaraan["bus"][pilihan_model]
    
    with col2:
        st.image(url_gambar, caption=f"Model: {pilihan_model}", use_column_width=True)
        st.info(f"Menampilkan: {pilihan_model}")

# Footer sederhana
st.markdown("---")
st.caption("Dibuat dengan Streamlit. Gambar diambil dari Wikimedia Commons.")
