import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title('E-Commerce Dashboard :sparkles:')

with st.sidebar:
    img_url = "https://github.com/antony-ch/assets-e-commerce-dashboard/blob/main/logo.jpg?raw=true"
    st.image(img_url, width=150)
    st.write("### E-Commerce")

    start_date = datetime(2018, 1, 1)
    end_date = datetime(2019, 12, 31)

    date_range = st.date_input(
    "Pilih rentang waktu",
    value=(start_date, end_date),
    min_value=datetime(2014, 1, 1),
    max_value=datetime(2019, 12, 31)
)

file_path = os.path.join(os.path.dirname(__file__), "all_data.csv")
df = pd.read_csv(file_path)

if "order_purchase_timestamp" in df.columns:
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    df = df[(df["order_purchase_timestamp"].dt.date >= date_range[0]) & 
            (df["order_purchase_timestamp"].dt.date <= date_range[1])]

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

if "product_category_name_english" in df.columns and "price" in df.columns:
    category_revenue = df.groupby("product_category_name_english")["price"].sum().reset_index()
    category_revenue = category_revenue.sort_values(by="price", ascending=False)

    top_5_revenue = category_revenue.head(5)

    st.subheader("📊 Top 5 Kategori Produk Berdasarkan Pendapatan")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(
        top_5_revenue["price"],
        labels=top_5_revenue["product_category_name_english"],
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Paired.colors
    )
    ax.set_title("Top 5 Kategori Produk Berdasarkan Pendapatan")
    ax.axis("equal")

    st.pyplot(fig)

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
