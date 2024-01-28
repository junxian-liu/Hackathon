import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# This one doesn't work
# def investing():
#     ticker = 'intel'
#     URL = f'https://www.investing.com/equities/{ticker}-corp-income-statement'
#     html = requests.get(URL)
#     soup = BeautifulSoup(html.content, "html.parser")

#     # web = soup.find('td', class_ = 'Ta(end) Fw(600) Lh(14px)').text
#     # web = soup.find_all('table')
#     web = soup.find('table', class_ = 'genTbl reportTbl').text
#     arr = web.split('\n')

#     while arr.count('') != 0:
#         arr.remove('')

#     while arr.count(' ') != 0:
#         arr.remove(' ')

#     dic = {}
#     for i in range(0, len(arr), 5):
#         dic[arr[i]] = arr[i+1: i+5]
#     dic['Period Ending:'] = [element[:4] + '-' + element[4:] for element in dic['Period Ending:']]

#     quarter_df = pd.DataFrame(dic).replace('-', np.NaN)
#     return quarter_df


def financial():
    ticker = input('Enter stock: ')
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

    return quarter_df.reset_index()


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

