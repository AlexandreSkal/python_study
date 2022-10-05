from select import select
from time import sleep
from binance.client import Client
from secrets import api_secret, api_key
import datetime

client = Client(api_key, api_secret)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE)
avg_price = client.get_avg_price(symbol='BTCUSDT')
prices = client.get_all_tickers()
'''candle_last_timestamp = datetime.datetime.fromtimestamp(int(candles[-1][0])/1000).strftime("%Y-%m-%d %H:%M:%S")
candle_last_open = candles[-1][1]
candle_last_high = candles[-1][2]
candle_last_low = ''
print(candle_last_timestamp)

while(1):
    print(f'Time: {candle_last_timestamp} - Open: {candle_last_open}')
    sleep(1)
#print(order_book['bids'][-1])
#print(candles[-1][0])'''

