#  token= 6320617649:AAGRBrKbz_KZIO-EqN7jQPk_l3pEawdcxWU

# chat_id= 6189684197 
from binanceAPI import get_order_book_binace
from kucoinAPI import get_order_book_kucoin
from time import sleep



class Arbitrage():
    def __init__(self) -> None:
        pass

    def chek_pair(self, coin, telbot, chatId):
        while True:
            pair = coin + "USDT"
            priceBinace = get_order_book_binace(pair=pair, limit=1)
            priceKu = 'BTC-USDT'
            priceKucoin = get_order_book_kucoin(pair=priceKu)

            if (priceBinace['check'] and priceKucoin['check']):
                buyKu = float(priceKucoin["buy"])
                sellBi = float(priceBinace["sell"])
                spreadBuyKu = (buyKu / sellBi - 1) * 100
                sellKu = float(priceKucoin["sell"])
                buyBi = float(priceBinace["buy"])
                spreadBuyBi = (buyBi / sellKu - 1) * 100

                if (spreadBuyKu > 0 ):
                    message = f'Спред: {spreadBuyKu}\nПокупаем на Binace, Цена: {priceBinace["sell"]}\n Продаем на Kucoin, Цена: {priceKucoin["sell"]}'
                    telbot.send_message(chatId, message)
                if(spreadBuyBi > 0):
                    messageLL = f'Спред: {spreadBuyBi}\nПокупаем на Kucoin, Цена: {priceKucoin["sell"]}\n Продаем на Binace, Цена: {priceBinace["sell"]}'
                    telbot.send_message(chatId, messageLL)
            sleep(60)