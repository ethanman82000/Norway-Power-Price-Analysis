import pandas as pd
import datetime as dt
import numpy as np

#import NordPool API to scrape day-ahead price data from online
from nordpool import elspot

def day_ahead_NP_prices(regions, year):
    # Set up market object
    spot = elspot.Prices()
        
    result = spot.daily(end_date=dt.date(year,1,1), areas=regions)
    
    # Initialise an empty list to store results
    all_data = []

    for i in regions:
        values = result['areas'][i]['values']
        all_data += [{"region": i, "date": entry['start'], "price": entry['value']} for entry in values]
    
    # Create DataFrame
    df = pd.DataFrame(all_data)

    df = pd.pivot_table(df, index=['date'], columns=['region'], values=['price']).droplevel(0, axis = 1)
    
    #Convert to datetime and sort
    df.index = pd.DatetimeIndex(df.index)

    return df
