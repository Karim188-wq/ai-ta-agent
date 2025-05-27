 import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="AI TA Agent", layout="centered")

st.title("AI Agent: Rule-Based Technical Analysis")
st.markdown("**By: @Karim188-wq**")

# Input saham dan tanggal
ticker = st.text_input("Masukkan kode saham atau crypto (contoh: AAPL, BTC-USD):", "AAPL")
start_date = st.date_input("Tanggal mulai", pd.to_datetime("2023-01-01"))
end_date = st.date_input("Tanggal akhir", pd.to_datetime("today"))

if st.button("Analisa"):
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        st.error("Data tidak ditemukan.")
    else:
        st.subheader("Data Harga")
        st.line_chart(data['Close'])

        # Rule-based TA sederhana
        data['SMA20'] = data['Close'].rolling(window=20).mean()
        data['SMA50'] = data['Close'].rolling(window=50).mean()

        latest = data.iloc[-1]

        st.subheader("Hasil Analisis:")
        if latest['SMA20'] > latest['SMA50']:
            st.success("Sinyal: **BUY** - Tren jangka pendek naik")
        elif latest['SMA20'] < latest['SMA50']:
            st.warning("Sinyal: **SELL** - Tren jangka pendek turun")
        else:
            st.info("Sinyal: **NEUTRAL**")

        st.subheader("Moving Averages")
        st.line_chart(data[['Close', 'SMA20', 'SMA50']])
