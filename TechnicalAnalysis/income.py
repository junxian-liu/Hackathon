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
    consolidated_df = quarter_df[['Sales/Revenue', 'Sales Growth', 'Gross Income']].drop(quarter_df.index[0])

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
    
def technical(ticker):

    company = financial(ticker)
    indicator = 0

    sales_rev = company.get('Sales/Revenue')
    sales_growth = company.get('Sales Growth')
    gross_income = company.get('Gross Income')

    if(sales_rev[0] > sales_rev[len(sales_rev) - 1]):
        indicator = 0.5
    else:
        indicator = -0.5

    if(sales_growth[0] > sales_growth[len(sales_growth) - 1]):
        indicator = indicator + 0.3
    else:
        indicator = indicator - 0.3

    if(gross_income[0] > gross_income[len(gross_income) - 1]):
        indicator = indicator + 0.2
    else:
        indicator = indicator - 0.2
    

    return indicator
