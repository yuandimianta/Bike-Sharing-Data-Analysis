import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour_df = pd.read_csv("https://raw.githubusercontent.com/yuandimianta/Bike-Sharing-Data-Analysis/main/data/hour.csv")

# Set page title
st.title("Bike Sharing Dashboard")

# Sidebar
st.sidebar.title("Menu")
selected_chart = st.sidebar.selectbox("Pilih Grafik", ["Pengaruh Musim", "Pengaruh Hari Kerja", "Pengaruh Hari Libur"])

# Fungsi untuk menggambar grafik
def draw_chart(data, x_label, y_label, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data['x'], y=data['y'], palette=data['color'], ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticklabels(data['labels'], rotation=45)
    st.pyplot(fig)

# Draw selected chart based on sidebar choice
if selected_chart == "Pengaruh Musim":
    seasonal_counts = hour_df.groupby('season')['cnt'].mean().reset_index()
    chart_data = {'x': seasonal_counts['season'], 'y': seasonal_counts['cnt'], 'color': sns.color_palette("pastel"), 'labels': ['Musim ' + str(int(x)) for x in seasonal_counts['season']]}
    draw_chart(chart_data, 'Musim', 'Rata-rata Jumlah Sewa Sepeda', 'Pengaruh Musim pada Jumlah Sewa Sepeda')

elif selected_chart == "Pengaruh Hari Kerja":
    workingday_counts = hour_df.groupby('workingday')['cnt'].mean().reset_index()
    chart_data = {'x': workingday_counts['workingday'], 'y': workingday_counts['cnt'], 'color': sns.color_palette("pastel"), 'labels': ['Bukan Hari Kerja', 'Hari Kerja']}
    draw_chart(chart_data, 'Hari Kerja', 'Rata-rata Jumlah Sewa Sepeda', 'Pengaruh Hari Kerja terhadap Jumlah Sewa Sepeda')

elif selected_chart == "Pengaruh Hari Libur":
    holiday_counts = hour_df.groupby('holiday')['cnt'].mean().reset_index()
    chart_data = {'x': holiday_counts['holiday'], 'y': holiday_counts['cnt'], 'color': sns.color_palette("pastel"), 'labels': ['Bukan Hari Libur', 'Hari Libur']}
    draw_chart(chart_data, 'Hari Libur', 'Rata-rata Jumlah Sewa Sepeda', 'Pengaruh Hari Libur terhadap Jumlah Sewa Sepeda')
