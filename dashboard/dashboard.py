import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('E-Commerce Dashboard :sparkles:')
 
with st.sidebar:
    
    img_url = "https://github.com/antony-ch/assets-e-commerce-dashboard/blob/main/logo.jpg?raw=true"
    st.image(img_url, width=150)
    st.write("### E-Commerce")

    start_date = datetime.today() - timedelta(days=30)
    end_date = datetime.today()

    date_range = st.date_input(
        "Pilih rentang waktu",
        value=(start_date, end_date),
        min_value=datetime(2020, 1, 1),
        max_value=datetime.today()
    )


df = pd.read_csv("all_data.csv")

if "customer_city" in df.columns:

    city_distribution = df["customer_city"].value_counts().reset_index()
    city_distribution.columns = ["customer_city", "customer_count"]

    top_10_cities = city_distribution.head(10)

    st.subheader("📊 Top 10 Kota dengan Jumlah Pelanggan Terbanyak")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_10_cities["customer_count"], y=top_10_cities["customer_city"], palette="Blues_r", ax=ax)
    ax.set_xlabel("Jumlah Pelanggan")
    ax.set_ylabel("Kota")
    ax.set_title("Top 10 Kota dengan Jumlah Pelanggan Terbanyak")

    st.pyplot(fig)
else:
    st.write("Kolom 'customer_city' tidak ditemukan dalam dataset.")


df = pd.read_csv("all_data.csv")

if "product_category_name" in df.columns:
  
    category_orders = df["product_category_name"].value_counts().reset_index()
    category_orders.columns = ["product_category_name", "order_count"]

   
    top_10_orders = category_orders.head(10)

    st.subheader("📊 Top 10 Kategori Produk Berdasarkan Jumlah Pesanan")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_10_orders["order_count"], y=top_10_orders["product_category_name"], palette="Paired", ax=ax)
    ax.set_xlabel("Jumlah Pesanan")
    ax.set_ylabel("Kategori Produk")
    ax.set_title("Top 10 Kategori Produk Berdasarkan Jumlah Pesanan")

    st.pyplot(fig)
else:
    st.write("Kolom 'product_category_name' tidak ditemukan dalam dataset.")


df = pd.read_csv("all_data.csv")

if "product_category_name_english" in df.columns and "price" in df.columns:

    category_revenue = df.groupby("product_category_name_english")["price"].sum().reset_index()

    category_revenue = category_revenue.sort_values(by="price", ascending=False)

    top_5_revenue = category_revenue.head(5)

    st.subheader("📊 Top 5 Kategori Produk Berdasarkan Jumlah Pendapatan")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(
        top_5_revenue["price"],
        labels=top_5_revenue["product_category_name_english"],
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Paired.colors
    )
    ax.set_title("Top 5 Kategori Produk Berdasarkan Jumlah Pendapatan")
    ax.axis("equal")

    st.pyplot(fig)
else:
    st.write("Kolom 'product_category_name_english' atau 'price' tidak ditemukan dalam dataset.")


df = pd.read_csv("all_data.csv")

if "payment_type" in df.columns:

    payment_counts = df["payment_type"].value_counts().reset_index()
    payment_counts.columns = ["payment_type", "count"]

    top_5_payments = payment_counts.head(5)

    st.subheader("📊 Top 5 Metode Pembayaran yang Paling Sering Digunakan")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_5_payments["payment_type"], y=top_5_payments["count"], palette="Blues_r", ax=ax)

    ax.set_xlabel("Metode Pembayaran")
    ax.set_ylabel("Jumlah Transaksi")
    ax.set_title("Top 5 Metode Pembayaran yang Paling Sering Digunakan")

    st.pyplot(fig)
else:
    st.write("Kolom 'payment_type' tidak ditemukan dalam dataset.")
