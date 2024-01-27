import requests
from bs4 import BeautifulSoup

url = "https://www.investing.com/equities/intel-corp"
html = requests.get(url)
data = html.text
soup = BeautifulSoup(data, 'html')
print(soup)