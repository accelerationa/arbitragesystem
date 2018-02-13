import requests
import csv
import json
import datetime
import time
from operator import itemgetter



url = "https://poloniex.com/public?command=returnTradeHistory&currencyPair=USDT_BTC&start=1518418000&end=%s" % str(int(time.time()))

response = requests.request("GET", url)
json_data = json.loads(response.text)

content = []

for data in json_data:
    t =time.mktime(datetime.datetime.strptime(str(data['date']), "%Y-%m-%d %H:%M:%S").timetuple())
    item = [t, data['tradeID'], data['rate'], data['amount']]
    content.append(item)

content = [['TimeStamp', 'Tid', 'Price', 'Amount']] + sorted(content, key=itemgetter(0))

print content

csvfile = open('poloniex_data.csv', 'a')
with csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(content)
print "Writing poloniex complete"

