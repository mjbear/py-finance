# Testing Python finance packages

Install [uv](https://docs.astral.sh/uv/pip/environments/) for Python package management

```bash
## Linux example
pip3.12 install uv --user
## Mac example
brew install uv
```

Then install Python dependencies with [uv](https://docs.astral.sh/uv/pip/environments/).

```bash
uv venv stocks
source stocks/bin/activate
uv pip install -r requirements.txt --native-tls
```

## 1. yfinance

Offers a Pythonic way to fetch financial & market data from Yahoo!&reg; finance.
Link: https://github.com/ranaroussi/yfinance/tree/main

### Example

```bash
⇨  python yfinance/stocks.py 
Market CAP: 207767.732224
Trailing P/E: 32.707424
Forward P/E: 20.899448
PEG: 7.4313
```

#### With plotly

```bash
⇨  python CandleSticks/candlesticks1.py
```

## 2. Quantitative Trading Strategies Using Python (Book)

First you need to unzip the data in [Quantitative_Trading/BenchmarkDatasets.zip].

### Example

From chapter 2.

```bash
⇨  cd Quantitative_Trading && python lob.py
(149, 254750)
Test
0     0.2615
4     0.2618
8     0.2619
12    0.2620
16    0.2621
20    0.2623
24    0.2625
28    0.2626
32    0.2629
36    0.2633
...
```

## 3. QuantStats 

#### From CSV data

```bash
⇨  python csv-test.py
HTML report saved to: rep.html
```

#### With streamlit

```bash
⇨  streamlit run stlit.py
```

## Troubleshooting

Make sure your DNS is not blocking `fc.yahoo.com` ([example](https://github.com/StevenBlack/hosts/issues/2708))

## Check out

- [Finance scripts](https://github.com/shashankvemuri/Finance/tree/master)
- [Awesome Systematic Trading](https://github.com/wangzhe3224/awesome-systematic-trading)
- [FRED: Federal Reserve Economic Data](https://fred.stlouisfed.org/)
