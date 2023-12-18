# https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT

import requests 

def get_order_book_kucoin(pair):
    orderBook = {}


    # pair = BTC-USDT
    url = f'https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol={pair}'
    

    respons = requests.get(url)
   
    if respons.status_code == 200:
        data = respons.json()
        orderBook['check'] = True 
        orderBook['buy'] = data['data']['bids'][0][0]
        orderBook['sell'] = data['data']['asks'][0][0]
    else:
        orderBook['check'] = False
    return orderBook
