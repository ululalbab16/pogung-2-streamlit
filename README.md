# 🌬️ Pogung V2.0 - Analisis Angin vs Gerah

### 📊 Temuan Utama
- **Mean Angin:** 2.10 (skala Beaufort modifikasi)
- **Mean Gerah:** 2.30
- **Korelasi:** -0.65 (korelasi negatif sedang)
- **Rumus Regresi:** `y = -0.76x + 3.65`
- **Interpretasi:** Tiap naik 1 level angin, rasa gerah turun 0.76 level. Terbukti angin mengurangi gerah!

### 🚀 Fitur V2.0
- [x] Dashboard interaktif (Streamlit)
- [x] 2 Mode Grafik: ALL 20 data & Per Tanggal (1 per 1)
- [x] Garis regresi otomatis
- [x] Tabel data lengkap (Waktu, Mendung, Warna Awan, Angin, Gerah)
- [x] Deploy online

### 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Matplotlib

### 📁 Data
20 observasi manual Pogung:
- 16 Okt: 2 data
- 17 Okt: 6 data
- 18 Okt: 7 data
- 19 Okt: 5 data
Variabel: Waktu, Mendung, Warna Awan, Angin (1-5), Gerah (1-5)

### 🔄 Evolusi Project
- **V1.1:** Script python `pogung.py` - analisis statistik dasar (repo: `analisis-angin-dan-gerah-pogung`)
- **V2.0:** Website interaktif + deploy Streamlit Cloud (repo ini)


---
*Dibuat dari error `pip not recognized` sampai jadi website online.*
