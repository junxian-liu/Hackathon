import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def financial(ticker):
    URL = f'https://www.marketwatch.com/investing/stock/{ticker}/financials/income/quarter'
    html = requests.get(URL)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find('table', class_ = 'table table--overflow align--right').text.split('\n')
    table = [element for element in table if element != '' and element != ' ']
    table.remove('5- qtr trend')

    dic = {}
    for i in range(0, len(table), 7):
        dic[table[i]] = table[i+2: i+7]

    quarter_df = pd.DataFrame(dic).replace('-', np.NaN)
    quarter_df.rename(columns = {'Item': 'Period Ending'}, inplace=True)
    quarter_df = quarter_df.set_index('Period Ending')

    for col in quarter_df.columns:
        quarter_df[col] = quarter_df[col].apply(convert_to_float)

    quarter_df.reset_index()
    consolidated_df = quarter_df[['Sales/Revenue', 'Sales Growth', 'Gross Income', 'Basic Shares Outstanding']]

    return consolidated_df


# Helper Function
def convert_to_float(item):
    if item != item:  # Check for NaN
        return np.NaN
    
    item = item.strip('()')
    if 'B' in item:
        return float(item[:-1])
    elif 'M' in item:
        return float(item[:-1]) / 1000
    elif '%' in item:
        return float(item[:-1]) / 100
    else:
        return float(item)