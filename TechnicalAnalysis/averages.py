# %%
from polygon import RESTClient
import pandas as pd
import numpy as np
import json
import time
from typing import cast
from urllib3 import HTTPResponse


def getData(ticker):
    tick = ticker
    client = RESTClient('Ao9fHerRTi5M9GteFUozhRdOasDXUXfN')
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

            
def getSMA(ticker):
    # Getting SMA (10)
    closingPrice = getData(ticker)
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
        indicator = 0.3
    elif (lastPrice < lastSMA10 and lastPrice < lastSMA50):
        indicator = -0.3
    else:
        indicator = 0

    return indicator


def getEMA(ticker):

    closingPrice = getData(ticker)

    df = pd.DataFrame({'Price' : closingPrice})

    ema_values = []
    alpha = 2 / 51  # EMA smoothing factor

    # Calculate initial EMA using SMA
    sma = sum(closingPrice[:50]) / 50
    ema_values.append(sma)

    # Calculate EMA for the remaining data points
    for i in range(50, len(closingPrice)):
        ema = (closingPrice[i] - ema_values[-1]) * alpha + ema_values[-1]
        ema_values.append(ema)

    last100_ema = ema_values[-100:]
    last100_price = closingPrice[-100:]
    counter = 0
    count = 0
    
    for num in last100_ema:
        if (num - last100_price[count] > 0):
            counter += 1

        count += 1
    
    if(counter > 75):
        indicator = 0.4
    else:
        indicator = -0.4

def calculate_rsi(ticker):
    closingPrice = pd.Series(getData(ticker))
    delta = closingPrice.diff()
    window = 7
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))


    # Checking if RSI is in oversold or overvalued range
    all_above_threshold = all(x > 70 for x in rsi[-30:])
    all_below_threshold = all(x <  30 for x in rsi[-30:])

    if(all_above_threshold):
        indicator = 0.6
    else:
        indicator = 0.2
    if(all_below_threshold):
        indicator = -0.6
    else:
        indicator = -0.2

    return indicator

# %%
