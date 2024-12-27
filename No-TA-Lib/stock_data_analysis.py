# https://www.pyquantnews.com/the-pyquant-newsletter/build-your-own-market-data-analytics-app-5-minutes

import streamlit as st
import pandas as pd
import yfinance as yf

def get_sp500_components():
    df = pd.read_html(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
    
    tickers = df["Symbol"].str.replace('.', '-').tolist()
    tickers_companies_dict = dict(zip(df["Symbol"], df["Security"]))
    return tickers, tickers_companies_dict

indicators = [ "Simple Moving Average",
               "Exponential Moving Average",
               "Relative Strength Index",
            ]

def apply_indicator(indicator, data):
    if indicator == "Simple Moving Average":
        data['SMA'] = data.Close.rolling(window=7).mean()
        return data[['Close', 'SMA']]
    
    elif indicator == "Exponential Moving Average":
        return data[['Close']]
    
    elif indicator == "Relative Strength Index":
        return data[['Close']]

st.title("Stock Data Analysis")
st.write("A simple app to download stock data and apply technical analysis indicators.")

st.sidebar.header("Stock Parameters")

available_tickers, tickers_companies_dict = get_sp500_components()

ticker = st.sidebar.selectbox(
    "Ticker", available_tickers, format_func=tickers_companies_dict.get
)

s = pd.Timestamp("2024-01-01")
start = st.sidebar.date_input("Start date:", s)

e = pd.Timestamp("2024-12-25")
end = st.sidebar.date_input("End date:", e)

data = yf.download(ticker, start, end, group_by='Ticker')
data = data.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

selected_indicator = st.selectbox("Select a technical analysis indicator:", indicators)

indicator_data = apply_indicator(selected_indicator, data)

st.write(f"{selected_indicator} for {ticker}")
st.line_chart(indicator_data)

st.write("Stock data for", ticker)
st.dataframe(data)