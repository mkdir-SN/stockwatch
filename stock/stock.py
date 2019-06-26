import requests
import json

# Class-based API handling

apikey = 'P6OBP81JQKGU00L8' # your API key here

def get_data(function, symbol, interval, size):
		url = 'https://www.alphavantage.co/query?function='+ str('time_series_' + function) + '&symbol=' + str(symbol) + '&interval=' + str(interval) + 'min&outputsize=' + str(size) + '&apikey=' + str(apikey)
		print(url)
		json_data = requests.get(url).json()
		return json_data

class Stock:

	def __init__(self, function, symbol, interval, size='compact'):
		self.function = function
		self.symbol = symbol
		self.interval = interval 
		self.size = size
		self.apikey = apikey
		self.json_data = get_data(function, symbol, interval, size)

	def __repr__(self):
		return str(self.symbol).upper()

	def is_valid(self): 
		try: 
			self.json_data['Meta Data']
		except KeyError:
			return False
		return True

	def stock_info(self):
		return [key[3:] + ': ' + self.json_data['Meta Data'][key] for key in self.json_data['Meta Data'].keys()]

	def stock_prices(self):
		prices_by_type = {'open': [], 'high': [], 'low': [], 'close': []}
		types = ['1. open', '2. high', '3. low', '4. close']
		for t in types:
			prices_by_type[t[3:]].extend(self.stock_type_prices(t))
		return prices_by_type
		
	def stock_type_prices(self, type):
		key = 'Time Series (' + str(self.interval) + 'min)'
		price_data = self.json_data[key]
		times = price_data.keys()
		return [float(price_data[t][type]) for t in times]

