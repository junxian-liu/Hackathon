# %%
import config
from polygon import RESTClient
import pandas as pd
import numpy as np
import json
import time
from typing import cast
from urllib3 import HTTPResponse


def getData(ticker):
    tick = ticker
    client = RESTClient(config.api_key)
    aggs = cast(
        HTTPResponse,
        client.get_aggs(
            tick, 
            1,
            'day', 
            '2023-01-01', 
            '2024-01-01', 
            raw = True
        )
    ) 

    data = json.loads(aggs.data)

    for item in data:
        if item == 'results':
            rawData = data[item]

    closingPrice = []
    for bar in rawData:
        for category in bar:
            if category == 'c':
                closingPrice.append(bar[category])

    return closingPrice

            
def getIndicator(closingPrice):
    # Getting SMA (10)
    df = pd.DataFrame({'Price' : closingPrice})
    window_size_10 = 10
    df['SMA-10'] = df['Price'].rolling(window=window_size_10).mean()

    #Getting SMA(50)
    window_size_50 = 50
    df['SMA-50'] = df['Price'].rolling(window=window_size_50).mean()


    # Price > SMA-10 & SMA-50 -> BUY | Price < SMA-10 & SMA-50 -> SELL
    # Indicator = True (BUY) | Indicator = False (SELL) | Indicator = None (Neither)

    sma_10 = df.get('SMA-10').to_numpy()
    sma_50 = df.get('SMA-50').to_numpy()

    lastPrice = closingPrice[len(closingPrice) - 1]
    lastSMA10 = sma_10[len(sma_10) - 1]
    lastSMA50 = sma_50[len(sma_50) - 1]
    
    if(lastPrice > lastSMA10 and lastPrice > lastSMA50):
        indicator = 0.1
    elif (lastPrice < lastSMA10 and lastPrice < lastSMA50):
        indicator = -0.1
    else:
        indicator = 0

    return indicator


def getEMA(closingPrice):

    df = pd.DataFrame({'Price' : closingPrice})

    #Getting EMA 12
    df_8 = df.iloc[-12:]
    nan = np.empty(22)
    nan.fill(np.nan)
    zero = nan.tolist()
    EMA_8 = zero + df_8['Price'].ewm(com = 0.4, adjust=False).mean().tolist()

    #Getting EMA 26
    df_20 = df.iloc[-26:]
    nan_list = np.empty(10)
    nan_list.fill(np.nan)
    zeros = nan_list.tolist()
    EMA_20 = zeros + df_20['Price'].ewm(com = 0.4, adjust=False).mean().tolist()


close = getData('TSLA')
getIndicator(close)
# %%
