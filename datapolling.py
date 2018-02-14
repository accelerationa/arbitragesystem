import requests
import csv
import json
import datetime
import time
from operator import itemgetter


map = {}

def get_trades_from_binance():
    url = "https://www.binance.com/api/v1/trades?symbol=BTCUSDT"

    try:
        response = requests.request("GET", url)
        json_data = json.loads(response.text)
    
        content = []

        for data in json_data:
            try:
                if int(str(data['time'])[:10]) not in map['binance'].keys():
                    item = [int(str(data['time'])[:10]), data['id'], data['price'], data['qty']]
                    content.append(item)
                    map['binance'][int(str(data['time'])[:10])] = True
            except:
                print '---------------- error condition happend ----------------'
                pass

        content = sorted(content, key=itemgetter(0))
        csvfile = open('binance_data.csv', 'a')
        with csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(content)
        print "Writing binance complete"

    except:
        print 'Error getting json data'
        pass


def get_trades_from_bittrex():
    url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market=USDT-BTC"

    try:
        response = requests.request("GET", url)
        json_data = json.loads(response.text)
        content = []

        for data in json_data['result']:
            try:        
                t =time.mktime(datetime.datetime.strptime(str(data['TimeStamp'][:19]), "%Y-%m-%dT%H:%M:%S").timetuple())
                t = t - 28800
                if t not in map['bittrex'].keys():
                    item = [t, data['Id'], data['Price'], data['Quantity'], data['OrderType']]
                    content.append(item)
                    map['bittrex'][t] = True
            except:
                print '---------------- error condition happend ----------------'
                pass
    
            
        content = sorted(content, key=itemgetter(0))
        csvfile = open('bittrex_data.csv', 'a')
        with csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(content)
        print "Writing bittrex complete"

    except:
        print 'Error getting json data'
        pass


def get_trades_from_bitfinex():
    url = "https://api.bitfinex.com/v1/trades/btcusd"

    try:
        response = requests.request("GET", url)
        json_data = json.loads(response.text)

        content = []
        for data in json_data:
            try:
                if int(data['timestamp']) not in map['bitfinex'].keys():
                    item = [int(data['timestamp']), data['tid'], data['price'], data['amount'], data['type']]
                    content.append(item)
                    map['bitfinex'][int(data['timestamp'])] = True
            except:
                print '---------------- error condition happend ----------------'
                pass

        content = sorted(content, key=itemgetter(0))
        csvfile = open('bitfinex_data.csv', 'a')
        with csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(content)
        print "Writing bitfinex complete"

    except:
        print 'Error getting json data'
        pass


if __name__ == "__main__":
    map = {
        'binance': {},
        'bittrex': {},
        'bitfinex': {}
    }
    
    #write title for each csv file
    content = [['TimeStamp', 'Tid', 'Price', 'Amount']]
    csvfile = open('binance_data.csv', 'a')
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)
    
    content = [['TimeStamp', 'Tid', 'Price', 'Amount', 'Type']]
    csvfile = open('bittrex_data.csv', 'a')
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)

    content = [['TimeStamp', 'Tid', 'Price', 'Amount', 'Type']]
    csvfile = open('bitfinex_data.csv', 'a')
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)

        
    while True:
        print datetime.datetime.now()
        get_trades_from_binance()
        get_trades_from_bittrex()
        get_trades_from_bitfinex()
        time.sleep(20) 


