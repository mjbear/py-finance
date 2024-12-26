import streamlit as st
import streamlit.components.v1 as components

import quantstats as qs

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

# fetch the daily returns for a stock
stock = qs.utils.download_returns('AAPL')
fig = qs.plots.snapshot(stock, title='AAPL Performance', show=False)
st.write(fig)

#qs.plots.snapshot(stock, title='Facebook Performance', show=True)
#qs.reports.full(stock, "SPY")


print("END")