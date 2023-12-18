import telebot 
from binanceAPI import get_prise_bts
from telebot import types
from mainbot import Arbitrage

token = "Token_TG"

telbot = telebot.TeleBot(token)

@telbot.message_handler(commands=["start"])
def start(message):
    item = types.InlineKeyboardMarkup(row_width=2)
    item2 = types.InlineKeyboardButton(text='Узнай сто процентов торговую пару btc/usdt', callback_data='yes2')
    item3 = types.InlineKeyboardButton(text='Арбитражим Бинанс/Кукоин', callback_data='yes3')
    item.add(item2, item3)

    telbot.send_message(message.chat.id, "Самые успешные хрипто инвесторы на районе", reply_markup=item)

# @telbot.message_handler(commands=["send_price_btc"])
# def send_price_btc(message):
#     price = get_prise_bts()
#     telbot.send_message(message.chat.id, f"Короче молодеш сейчас ващ битховен ака BTC к долару торгуется на краснодарских рынках в райоНАХ {price}, цифры точные так что не паникуй")
#     telbot.send_message(message.chat.id, f"Хочешь больше торговых пар закидывай на USDT")


@telbot.callback_query_handler(func=lambda call:True)
def callbeck(call):
    if call.message:
        if call.data == "yes2":
            price = get_prise_bts()
            telbot.send_message(call.message.chat.id, f"Короче молодеш сейчас ващ битховен ака BTC к долару торгуется на краснодарских рынках в райоНАХ {price}, цифры точные так что не паникуй")
            telbot.send_message(call.message.chat.id, f"Хочешь больше торговых пар закидывай на USDT")
        if call.data == "yes3":
            arbitrage = Arbitrage()
            arbitrage.chek_pair("BTC", telbot, call.message.chat.id)

# @telbot.message_handler(commands=["run_check_btc"])
# def check_btc(message):
#     arbitrage = Arbitrage()
#     arbitrage.chek_pair("BTC", telbot, message.chat.id)
    # telbot.send_message(message.chat.id, messageSpread)

telbot.infinity_polling()



    