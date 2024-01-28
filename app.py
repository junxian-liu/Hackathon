from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_algorithm', methods=['POST'])
def run_algorithm():
    try:
        data = request.get_json()
        print('Received data:', data)
        result = process_data(data)
        print('Result:', result)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
    
def process_data(data):
    # From Income file
    print('Starting Flask app...')
    ticker = data['input']
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

if __name__ == '__main__':
    app.run(debug=True)
    
    