import yfinance as yf
# Create Ticker object
stock = yf.Ticker("IBM")

# Fetch stock info
try:
    info = stock.info
except Exception as e:
    print(f"Error: {e}")

print("Market CAP: " + str(info['marketCap'] / 1000000))
print("Trailing P/E: " + str(info['trailingPE']))
print("Forward P/E: " + str(info['forwardPE']))
print("PEG: " + str(info['trailingPegRatio']))
