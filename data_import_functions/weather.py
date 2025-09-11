import pandas as pd
import datetime as dt
import numpy as np

#import requests to query the Frost API
import requests

#import dotenv to load client_ID secret key
from dotenv import load_dotenv
import os

from config import PROJECT_ROOT
load_dotenv(PROJECT_ROOT / ".env")
client_id = os.getenv("FROST_CLIENT_ID")

#Querying Frost API for the relevant sources: I am finding all weather stations in the county of Agder and treating the averaged measurements as representative/indicative of the weather condition in Southern Norway.
#All stations in Agder (found in prev cell) are queried for their max air temp, total precip, and mean wind speed - all aggregations of measurements are taken over the period of a day.
#A dataframe is returned and pivoted out to have the weather observations as col headers
#Finally, the data is grouped day by day and the mean of each variable taken to generate representative values for Southern Norway.

def Frost_weather_data(year):
    endpoint = "https://frost.met.no/sources/v0.jsonld"
    params = {
        'county': 'AGDER',
        #"nearestmaxcount": 3
    }
    response = requests.get(endpoint, params, auth=(client_id, ""))
    agder_ids = [station.get('id') for station in response.json()['data']]
    agder_source_ids = ','.join(agder_ids)
    
    # Define endpoint and parameters
    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': agder_source_ids,
        'elements': 'max(air_temperature P1D), mean(wind_speed P1D), sum(duration_of_sunshine P1D)',
        'referencetime': f'{year}-01-01/{year+1}-01-01',
        #'timeresolutions': 'P1D',
        #to limit observations to 1 for each source/element/ref_time combination
        #'timeoffsets': 'PT6H',
        #'levels': '2',
    }
    # Issue an HTTP GET request
    r = requests.get(endpoint, parameters, auth=(client_id,''))
    # Extract JSON data
    json = r.json()
    
    # Check if the request worked, print out any errors
    if r.status_code == 200:
        data = json['data']
        print('Data retrieved from frost.met.no!')
    else:
        print('Error! Returned status code %s' % r.status_code)
        print('Message: %s' % json['error']['message'])
        print('Reason: %s' % json['error']['reason'])

    #flatten json data and gather weather and time data
    #pivot this out and average over time slices to give representative weather data at a certain time
    df = pd.json_normalize(data, record_path = 'observations', meta = ['referenceTime'], max_level = 0)
    weather_table = df.groupby(['referenceTime', 'elementId'])['value'].mean().unstack('elementId')
    weather_table.index = pd.DatetimeIndex(weather_table.index).tz_localize(None)

    return weather_table
    
    
