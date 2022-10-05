from websocket import WebSocketApp
import json
from binance.client import Client
from binance.enums import *
from secrets import api_secret, api_key
client = Client(api_key, api_secret)
ordem = False

par_moedas = 'btcusdt'
socket = f'wss://stream.binance.com:9443/ws/{par_moedas}@bookTicker'

balance = client.get_asset_balance(asset='usdt')
print(balance)

order = client.create_order(
    symbol='BTCUSDT',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=0.002)
print(order)


def on_message(ws, message):
    json_message = json.loads(message)
    print('Price: ' + json_message['a'])


def on_close(ws):
    print('### Closed ###')


ws = WebSocketApp(socket, on_message=on_message, on_close=on_close)
ws.run_forever()
