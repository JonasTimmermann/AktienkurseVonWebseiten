import requests
from bs4 import BeautifulSoup
import time


i = 0
while i < 20 :
    url2 = 'https://www.finanzen.net/aktien/wirecard-aktie' 

    res2 = requests.get( url2 )
    html2 = res2.text


    soup2 = BeautifulSoup( html2, 'html.parser' )
    mydivs = soup2.findAll("div", {"class": "col-xs-5 col-sm-4 text-sm-right text-nowrap"})
    #print(mydivs[0])
    stri = mydivs[0]
    #print(stri)
    soup3 = BeautifulSoup(stri.text, 'lxml')
    print(soup3.text)
    time.sleep(120)
    i+=1




"""

#### 2. Version ####

ticker = 'AAPL'
url = 'https://de.finance.yahoo.com/quote/' + ticker
# url = 'https://de.finance.yahoo.com/quote/' + ticker

res = requests.get( url )
html = res.text

soup = BeautifulSoup( html, 'html.parser' )
market_cap_elem = soup.find( 'td', { 'data-test' : 'MARKET_CAP-value' } )
market_cap_elem2 = soup.find( 'td', { 'data-test' : 'PREV_CLOSE-value' } )
market_cap = market_cap_elem.text
prev = market_cap_elem2.text

print( ticker, 'Market Cap', market_cap )
print( ticker, 'Vortag', prev )

"""