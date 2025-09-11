import pandas as pd
import datetime as dt

from config import DATA_DIR, SOURCE_DIR

def reservoir_levels(year):
    res_lvl = pd.read_csv(DATA_DIR / "Water_Reservoir_Filling_Data_entsoe.csv", na_values = '-')
    res_lvl = res_lvl.drop(columns = ['Week'], index = 52).astype('float').div(10**6)
    res_lvl.columns = res_lvl.columns.astype('int')
    years_after = res_lvl.columns[res_lvl.columns >= year]
    res_lvl['Hist_Avg'] = res_lvl.drop(columns = years_after).mean(axis=1)
    res_lvl['Anomaly'] = (res_lvl[year] - res_lvl.Hist_Avg)
    res_lvl.index = pd.Index(res_lvl.index.values + 1, name = 'Week')

    return res_lvl[[year, 'Anomaly']].rename(columns={year: 'Reservoir stores', 'Anomaly': 'Storage anomaly'})
