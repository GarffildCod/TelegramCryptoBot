import requests 

# https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT

# https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=2


def get_prise_bts():
    symbol = "BTCUSDT"

    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    respons = requests.get(url)

    if respons.status_code == 200:
        data = respons.json()
        return data['price']
    else:
        print("error:", respons.status_code)

def get_order_book_binace(pair, limit):
    orderBook = {}

    url = f'https://api.binance.com/api/v3/depth?symbol={pair}&limit={limit}'

    respons = requests.get(url)

    if respons.status_code == 200:
        data = respons.json()
        orderBook['check'] = True 
        orderBook['buy'] = data['bids'][0][0]
        orderBook['sell'] = data['asks'][0][0]
    else:
        orderBook['check'] = False
    
    return orderBook


