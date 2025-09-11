import pandas as pd

from config import DATA_DIR, SOURCE_DIR

def UK_prices(year):
    european_prices = pd.read_csv(DATA_DIR / "EU_daily_price_data_Ember.csv")
    european_prices['Date'] = pd.to_datetime(european_prices['Date'], dayfirst= True)
    UK_price = european_prices[(european_prices['ISO3 Code'] == 'GBR') & (european_prices['Date'].dt.year == year)].rename(columns={'Price (EUR/MWhe)': 'UK'})
    UK_price.index = pd.DatetimeIndex(UK_price['Date'])

    return UK_price['UK']
