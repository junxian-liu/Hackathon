from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, request, render_template
from TechnicalAnalysis import averages

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    ticker = request.form["ticker"]
    indicator = averages.calculate_rsi(ticker) 
    print(indicator)
    return render_template('pass.html', ind = indicator)
     

if __name__ == '__main__':
    app.run(debug=True)


