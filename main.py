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
    ticker = request.form["ticker"]
    print(income.financial(ticker))
    indicator = getIndicator(ticker)
    return render_template('index.html', ind = indicator)
     

def getIndicator(ticker):
    indicators = []

    #moving averages
    sma = averages.getSMA(ticker)
    ema = averages.getEMA(ticker)
    rsi = averages.calculate_rsi(ticker)

    #finance
    company = finance.similarCompany(ticker)
    financial = finance.analysis(company)

    indicators.append(sma)
    indicators.append(ema)
    indicators.append(rsi)
    indicators.append(financial)
    
    ind = sum(indicators) / len(indicators)
    return ind

if __name__ == '__main__':
    app.run(debug=True)


