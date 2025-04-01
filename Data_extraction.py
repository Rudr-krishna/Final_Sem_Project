import yfinance as yf
import pandas as pd

companies_ticker = ['AAPL', 'MSFT', 'TSLA', 'AMZN', 'NVDA']

for val in companies_ticker:
    df = yf.download(val, period="1y", interval="1d")
    df.to_csv(f'{val}_data.csv')
    print(f'Stocks data of {val} is download and stored.')