import requests
import json

# Class-based API handling

apikey = 'P6OBP81JQKGU00L8' # your API key here

def get_data(function, symbol, interval, size): 
		url = 'https://www.alphavantage.co/query?function='+ str('time_series_' + function) + '&symbol=' + str(symbol) + '&outputsize=' + str(size) + '&apikey=' + str(apikey)
		if function == 'Intraday':
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
		# Returns string format of stock information
		return [key[3:] + ': ' + self.json_data['Meta Data'][key] for key in self.json_data['Meta Data'].keys()]

	def stock_symbol(self):
		return self.symbol

	def stock_prices(self):
		# Returns re-structured dictionary of the different prices to fit Chart.js datasets
		prices_by_type = {'open': [], 'high': [], 'low': [], 'close': []}
		types = ['1. open', '2. high', '3. low', '4. close']
		for t in types:
			prices_by_type[t[3:]].extend(self.stock_type_prices(t))
		return prices_by_type

	def stock_key(self):
		# Returns which key should be used to dive into JSON API response based on time series
		key = str(self.function) + ' Time Series'
		if self.function == 'Intraday':
			key = 'Time Series (' + str(self.interval) + 'min)'
		elif self.function == 'Daily':
			key = 'Time Series (Daily)'
		return key

	def stock_times(self):
		# Returns stock times (a string) i.e. '2019-07-01', '2019-07-01 13:30:00'
		key = self.stock_key()
		price_data = self.json_data[key]
		times = list(price_data.keys())
		list.reverse(times) # To account for descending order of date in JSON response
		return times
		
	def stock_type_prices(self, type):
		# Returns stock prices (a list) associated with one of the following stock types (a string): open, high, low, close
		key = self.stock_key()
		price_data = self.json_data[key]
		times = price_data.keys()
		stock_type_prices = [float(price_data[t][type]) for t in times]
		list.reverse(stock_type_prices) # to account for descending order of date in JSON response
		return stock_type_prices

	def stock_time_and_prices(self):
		# Returns a list where each embedded list is [stock time (a string), a dictionary affiliated with stock time]
		stock_time_and_prices = zip(stock_times, stock_prices)
		return stock_time_and_prices
