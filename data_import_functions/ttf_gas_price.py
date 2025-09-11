import pandas as pd
import datetime as dt

import yfinance as yf

def ttf_gas(year):
    ticker = yf.Ticker('TTF=F')
    ttf_gas = ticker.history(start=dt.date(year,1,1), end=dt.date(year+1,1,1))
    ttf_gas.index = pd.to_datetime(ttf_gas.index.date)
    return ttf_gas['Close'].rename('Gas Price')
