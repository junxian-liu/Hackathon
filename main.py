from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, request, render_template
from TechnicalAnalysis import averages, finance, income

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    ticker = request.form["ticker"].upper()
    #List of weights from all analysis
    indicator = getIndicator(ticker)
    #Indicator
    ind = sum(indicator) / len(indicator)
    if(ind > 0.2):
        ind_name = "BUY🚀"
    elif(ind > -0.2):
        ind_name = "HOLD🙉"
    else:
        ind_name = "SELL🥱"
    #Statement summarizing analysis
    statement = financialReports(ind, indicator, ticker)
    #Send values back to website
    img_path = "url_for('static', filename='images/happy.png')"
    return render_template('index.html', ind_val = ind_name, state = statement)
     

def getIndicator(ticker):
    indicators = []

    #moving averages
    sma = averages.getSMA(ticker)
    ema = averages.getEMA(ticker)
    rsi = averages.calculate_rsi(ticker)

    #finance
    company = finance.similarCompany(ticker)
    financial = finance.analysis(company)

    #income
    income_sheet = income.technical(ticker)

    indicators.append(sma)
    indicators.append(ema)
    indicators.append(rsi)
    indicators.append(financial)
    indicators.append(income_sheet)
    
    return indicators

def financialReports(indicator, values, ticker):
    sma_statement = ""
    ema_statement = ""
    rsi_statement = ""
    financial_statement = ""
    income_statement = ""
    final_statement = ""

    #SMA
    if(values[0] > 0):
        sma_statement = f"{ticker}'s recent SMA values indicate that the stock is moving inline with a bullish trend. "
    else: 
        sma_statement = f"{ticker}'s recent SMA values indicate that the stock is moving inline with a bearish trend. "
    #EMA
    if(values[1] > 0):
        ema_statement = f"{ticker}'s recent EMA values correlate with a uptrend as signified with the SMA values. "
    else: 
        ema_statement = f"{ticker}'s recent EMA values correlate with a downtrend as signified with the SMA values. " 
    #RSI
    if(values[2] > 0.5):
        rsi_statement = f"{ticker}'s RSI value illustrate the stock being oversold, showing great signs to rebound. "
    elif(values[2] < 0.5): 
        rsi_statement = f"{ticker}'s RSI value illustrate the stock beind overvalued, showing great signs to decline. " 
    else:
        rsi_statement = f"{ticker}'s RSI value is between oversold and overvalued, not showing significant weight to a rebound or decline. "
    #EPS and P/E Ratio
    if(values[3] > 0):
        financial_statement_statement = f"{ticker}'s EPS and P/E ratio is are more valued compared to their competitors. "
    else: 
        financial_statement_statement = f"{ticker}'s EPS and P/E ratio is lacking compared to their competitors. "
    #Income
    if(values[4] > 0):
        financial_statement_statement = f"{ticker}'s income statement show signs of increasing growth in the company. "
    else: 
        financial_statement_statement = f"{ticker}'s income statement show signs of decreasing growth in the company. "  

    #BUY
    if(indicator > 0.2):
        final_statement = f"Based on this analysis, that's why we belive {ticker} is a BUY!"
    elif(indicator < -0.2):
        final_statement = f"Based on this analysis, that's why we belive {ticker} is a SELL!"
    else:
        final_statement = f"Based on this analysis, that's why we belive {ticker} is a HOLD!"


    statement = sma_statement + ema_statement + rsi_statement + financial_statement + income_statement + final_statement

    return statement


if __name__ == '__main__':
    app.run(debug=True)


