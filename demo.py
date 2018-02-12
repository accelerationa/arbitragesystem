import requests
import csv
import json
import datetime
import time


map = {}

def get_trades_from_binance():
    url = "https://www.binance.com/api/v1/trades?symbol=BTCUSDT"

    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    content = []

    for data in json_data:
        if int(str(data['time'])[:10]) not in map['binance'].keys():
            item = [int(str(data['time'])[:10]), data['id'], data['price'], data['qty']]
            content.append(item)
            map['binance'][int(str(data['time'])[:10])] = True


    content = [['TimeStamp', 'Tid', 'Price', 'Amount']] + content
    csvfile = open('binance_data.csv', 'a')
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)
    print "Writing binance complete"


def get_trades_from_bittrex():
    url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market=USDT-BTC"

    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    content = []

    for data in json_data['result']:
        item = [data['TimeStamp'], data['Id'], data['Price'], data['Quantity'], data['OrderType']]
        content.append(item)

    content = [['TimeStamp', 'Tid', 'Price', 'Amount', 'Type']] + content
    csvfile = open('bittrex_data.csv', 'a')
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)
    print "Writing bittrex complete"



def get_trades_from_bitfinex():
    url = "https://api.bitfinex.com/v1/trades/btcusd"

    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    content = []
    for data in json_data:
        item = [datetime.datetime.fromtimestamp(int(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'), data['tid'], data['price'], data['amount'], data['type']]
        content.append(item)

    content = [['TimeStamp', 'Tid', 'Price', 'Amount', 'Type']] + content
    csvfile = open('bitfinex_data.csv', 'a')
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)
    print "Writing bitfinex complete"



if __name__ == "__main__":
    map = {
        'binance': {},
        'bittrex': {},
        'bitfinex': {}
    }

    while True:
        get_trades_from_binance()

    # while True:
    #     get_trades_from_binance()
    #     get_trades_from_bittrex()
    #     get_trades_from_bitfinex()
    #     time.sleep(20) 


