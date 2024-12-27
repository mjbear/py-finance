# https://www.pyquantnews.com/the-pyquant-newsletter/build-your-own-market-data-analytics-app-5-minutes

import streamlit as st
import pandas as pd
import yfinance as yf
import talib
import numpy as np

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
        #sma = talib.SMA(data["Close"].values)
        sma = data.Close.apply(lambda c: talib.SMA(c))
        return sma
        #return pd.DataFrame({"Close": data["Close"], "SMA": sma})
    
    elif indicator == "Exponential Moving Average":
        #ema = talib.EMA(data["Close"].values)
        ema = data.Close.apply(lambda c: talib.EMA(c))
        return ema
        #return pd.DataFrame({"Close": data["Close"], "EMA": ema})
    
    elif indicator == "Relative Strength Index":
        #rsi = talib.RSI(data["Close"].values)
        rsi = data.Close.apply(lambda c: talib.RSI(c))
        return rsi
        #return pd.DataFrame({"Close": data["Close"], "RSI": rsi})

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

data = yf.download(ticker, start, end)

selected_indicator = st.selectbox("Select a technical analysis indicator:", indicators)

ta = apply_indicator(selected_indicator, data)
dc = data.Close
dc[selected_indicator] = ta.loc[s:e]

indicator_data = dc.rename(columns={ticker: "Close"})

st.write(f"{selected_indicator} for {ticker}")
st.line_chart(indicator_data)

st.write("Stock data for", ticker)
st.dataframe(data)