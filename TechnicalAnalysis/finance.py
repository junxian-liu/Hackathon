import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def getSingleCompany(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    html = requests.get(url)

    s = BeautifulSoup(html.content, "html.parser")

    similar = s.find('section', id = 'similar-by-symbol')
    companys = similar.find_all('a', class_= 'Fw(b) Ell D(b) C($linkColor) Pos(r) Z(2)')

    company_similar_ticker = [ticker]
    len(companys)

    for i in range(len(companys)):
        company_similar_ticker.append(companys[i].text)

    return company_similar_ticker

def similarCompany(ticker):
    company_similar_ticker = getSingleCompany(ticker)
    company_name = []
    curr_price = []
    mar_cap = []
    per = []
    earnings = []

    for tick in company_similar_ticker:
        url_1 = f"https://finance.yahoo.com/quote/{tick}?p={tick}"

        html_1 = requests.get(url_1)
        t = BeautifulSoup(html_1.content, "html.parser")

        results = t.find(id = 'Lead-5-QuoteHeader-Proxy')
        comp_title = results.find_all('h1', class_= 'D(ib) Fz(18px)')[0].text
        cur_price = results.find_all('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)')[0].text

        financial = t.find(id = 'Main')
        curr_financials = financial.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')   

        market_cap = curr_financials[8].text
        pe_ratio = curr_financials[10].text
        eps = curr_financials[11].text  
        
        company_name.append(comp_title)
        curr_price.append(cur_price)
        mar_cap.append(market_cap)
        per.append(pe_ratio)
        earnings.append(eps)


    similar_dict = {'Tickers': company_similar_ticker, 'Company Name': company_name, 'Current Price': curr_price, 'Market Cap': mar_cap, 'P/E Ratio': per, 'EPS': earnings}
    similar_df = pd.DataFrame(similar_dict)
    similar_df["Current Price"] = similar_df["Current Price"].str.replace(",","").astype(float)
    similar_df["EPS"] = similar_df["EPS"].str.replace(",","").astype(float)
    per = similar_df.get('Current Price').replace(",", "").astype(float) / similar_df.get('EPS').replace(",", "").astype(float)
    similar_df['P/E Ratio']= per
    
    return similar_df

def analysis(df):
    company = df

    indicator = 0

    main_PE = float(df.loc[0, 'P/E Ratio'])
    main_EPS = float(df.loc[0, 'EPS'])

    if((main_PE < 0) or (main_EPS < 0)):
        indicator = -1

    #Comparing EPS against similar companies
    eps_comparison = main_EPS > df.get('EPS').astype(float)
    if(eps_comparison.sum() > len(eps_comparison) * 0.8):
        print(eps_comparison.sum(), len(eps_comparison) * 0.66)
        indicator = 0.6

    if(main_PE > 0.25):
        if(indicator != 0):
            indicator = indicator * 0.5
        else:
            indicator = -0.6
    else:
        if(indicator != 0):
            indicator = indicator * 2
        else:
            indicator = 0.6

    return indicator
