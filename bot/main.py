from websocket import WebSocketApp
import json

par_moedas = 'btcusdt'
intervalo = '1m'
socket = f'wss://stream.binance.com:9443/ws/{par_moedas}@kline_{intervalo}'


def on_message(ws, message):
    json_message = json.loads(message)
    cs = json_message['k']
    candle_closed, close, high, low = cs['x'], cs['c'], cs['h'], cs['l']
    print(candle_closed)
    print(close)
    print(high)
    print(low)


def on_close(ws):
    print('### Closed ###')


ws = WebSocketApp(socket, on_message=on_message, on_close=on_close)
ws.run_forever()
