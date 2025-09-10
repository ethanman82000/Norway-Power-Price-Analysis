import pandas as pd

from .weather import Frost_weather_data
from .eu_spots import day_ahead_NP_prices
from .uk_spot import UK_prices
from .ttf_gas_price import ttf_gas
from .reservoir_levels import reservoir_levels

def extract_data_from(year):
    df = pd.concat([Frost_weather_data(year), day_ahead_NP_prices(['NO2','GER','DK1','NL'], year), UK_prices(year), ttf_gas(year)], join = 'outer', axis = 1)
    df['Week'] = df.index.isocalendar().week
    df = df.join(reservoir_levels(year), on = 'Week', how = 'right')
    df['Gas Price'] = df['Gas Price'].ffill(limit=2).bfill(limit=2)
    return df
