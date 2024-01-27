import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def investing():
    ticker = 'intel'
    URL = f'https://www.investing.com/equities/{ticker}-corp-income-statement'
    html = requests.get(URL)
    soup = BeautifulSoup(html.content, "html.parser")

    # web = soup.find('td', class_ = 'Ta(end) Fw(600) Lh(14px)').text
    # web = soup.find_all('table')
    web = soup.find('table', class_ = 'genTbl reportTbl').text
    arr = web.split('\n')

    while arr.count('') != 0:
        arr.remove('')

    while arr.count(' ') != 0:
        arr.remove(' ')

    dic = {}
    for i in range(0, len(arr), 5):
        dic[arr[i]] = arr[i+1: i+5]
    dic['Period Ending:'] = [element[:4] + '-' + element[4:] for element in dic['Period Ending:']]

    quarter_df = pd.DataFrame(dic).replace('-', np.NaN)
    return quarter_df


def financial(firm):
    ...