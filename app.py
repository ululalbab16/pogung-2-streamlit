import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pogung V2.0 - Angin vs Gerah", layout="wide")
st.title("Pogung V2.0 - Angin vs Gerah")
st.caption("Data asli 20 observasi - 16-19 Okt 2026 - Rumus y = -0.76x + 3.65")

data = [
    ["16 Okt","15:00",2,"Hitam 1/4",2,2],
    ["16 Okt","17:00",1,"Cerah",2,2],
    ["17 Okt","09:00",0,"Tidak ada awan",1,4],
    ["17 Okt","10:00",0,"Cerah",0,5],
    ["17 Okt","12:00",3,"Cerah",2,3],
    ["17 Okt","13:00",3,"1/4 Awan Mendung",2,2],
    ["17 Okt","14:00",2,"1/8 awan mendung",3,2],
    ["17 Okt","16:00",1,"Cerah",4,1],
    ["18 Okt","05:30",2,"1/8 Awan Mendung",2,1],
    ["18 Okt","08:00",4,"1/4 Awan Mendung",3,2],
    ["18 Okt","09:30",3,"Cerah",1,3],
    ["18 Okt","10:30",3,"1/3 Awan Mendung",1,4],
    ["18 Okt","13:30",5,"1/4 Awan Mendung",3,1],
    ["18 Okt","14:30",2,"1/4 Awan Mendung",3,2],
    ["18 Okt","16:00",5,"1/2 Awan Mendung",3,1],
    ["19 Okt","06:30",4,"1/4 Awan Mendung",1,1],
    ["19 Okt","09:30",3,"1/8 Awan Mendung",1,1],
    ["19 Okt","12:00",2,"Cerah",2,2],
    ["19 Okt","15:30",2,"Cerah",3,1],
    ["19 Okt","16:30",3,"1/8 Angin Mendung",3,1],
]
df = pd.DataFrame(data, columns=["Tanggal","Waktu","Mendung","Warna_Awan","Angin","Gerah"])

# --- PILIH MODE ---
mode = st.radio("Mode Grafik:", ["ALL 16-19 Okt (20 data)", "Per Tanggal (1 per 1)"], horizontal=True)

if mode == "ALL 16-19 Okt (20 data)":
    df_plot = df
    judul = "ALL DATA 16-19 Okt (20 observasi)"
else:
    tanggal = st.selectbox("Pilih Tanggal:", df["Tanggal"].unique())
    df_plot = df[df["Tanggal"] == tanggal]
    judul = f"Data {tanggal} - {len(df_plot)} observasi"

col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader(judul)
    st.dataframe(df_plot, use_container_width=True, hide_index=True)
    st.metric("Rata-rata Angin", f"{df_plot['Angin'].mean():.2f}", f"{len(df_plot)} data")
    st.metric("Rata-rata Gerah", f"{df_plot['Gerah'].mean():.2f}")

with col2:
    st.subheader("Grafik ANGIN vs GERAH")
    fig, ax = plt.subplots()
    ax.scatter(df_plot["Angin"], df_plot["Gerah"], s=80)
    
    # Garis rumus kamu
    x_line = [0, 4]
    y_line = [-0.76*x + 3.65 for x in x_line]
    ax.plot(x_line, y_line, linestyle='--', label='y=-0.76x+3.65')
    
    ax.set_xlabel("Angin (0-4)")
    ax.set_ylabel("Gerah (1-5)")
    ax.set_title(judul)
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    st.caption("Semakin kencang angin (kanan), gerah turun (bawah)")

st.divider()
st.subheader("Prediksi")
angin_input = st.slider("Input Angin", 0, 4, 2)
pred = -0.76*angin_input + 3.65
st.metric("Prediksi Gerah", f"{pred:.2f}")