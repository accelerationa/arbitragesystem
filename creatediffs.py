from pandas import Series
from matplotlib import pyplot
import pandas as pd
from pandas.plotting import lag_plot
from pandas import concat
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt


import csv


# bittrex_data   binance_data    bitfinex_data    poloniex_data

PRECISION = 20

items = []
content = []

with open('poloniex_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
		try:
			row['TimeStamp'] = str(float(row['TimeStamp']) - float(row['TimeStamp']) % PRECISION)
			items.append([row['TimeStamp'], row['Price']])
		except:
			pass

print items
		
i = 0
while i < len(items):
	if i != 0 and float(items[i][0]) - float(content[-1][0]) > PRECISION:
		content.append([float(content[-1][0])+PRECISION, content[-1][1]])
		continue
	if i == 0 or items[i][0] != items[i-1][0]:
		content.append(items[i])
	i += 1

print content

csvfile = open('data.csv', 'w')
with csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(content)





		

