import requests
from bs4 import BeautifulSoup as bs

def get_symbol_name(symbol):
    """
    symbol -- must be from cmc
    https://coinmarketcap.com/currencies/ CRYPTO-NAME /
    """
    html = requests.get(f"https://coinmarketcap.com/currencies/{symbol}/")
    if html.status_code != 200:
        print(f"Error while getting symbol name {html.status_code}.")
        return
    text = bs(html.content, 'html.parser') 
    return text.find("small").text

def get_eur_price():
    html = requests.get("https://coinmarketcap.com/currencies/stasis-euro/")
    if html.status_code != 200:
        print(f"Error while getting symbol name {html.status_code}.")
    text = bs(html.content, 'html.parser') 
    return float(text.find("div", {"class":"priceValue"}).text.replace("$",""))