from django.db import models
from django import forms
from stock.models import Ticker
import requests
import json

apikey = "P6OBP81JQKGU00L8"

def get_data(function, symbol, interval, size):
		url = "https://www.alphavantage.co/query?function="+ str(function) + "&symbol=" + str(symbol) + "&interval=" + str(interval) + "min&outputsize=" + str(size) + "&apikey=" + str(apikey)
		print(url)
		json_data = requests.get(url).json()
		return json_data

class Stock:

	def __init__(self, function, symbol, interval, size):
		self.function = function
		self.symbol = symbol
		self.interval = interval # 1min, 5min, 15min, 30min, 60min
		self.size = size
		self.apikey = apikey
		self.json_data = get_data(function, symbol, interval, size)

	def __repr__(self):
		return str(self.symbol)

	def is_valid(self): 
		try: 
			self.json_data['Meta Data']
		except KeyError:
			return False
		return True

	def stock_info(self):
		return [self.json_data['Meta Data'][key] for key in self.json_data['Meta Data'].keys()]

	def stock_prices(self):
		key = 'Time Series (' + self.interval + 'min)'
		return self.json_data[key]

class TickerForm(forms.ModelForm): 

	class Meta:
		model = Ticker
		fields = ['ticker']

	def __init__(self, *args, **kwargs): # override init to access request.user from stock.views
         self.user = kwargs.pop('user')
         super(TickerForm, self).__init__(*args, **kwargs)

	def clean_ticker(self):
		ticker = self.cleaned_data['ticker']
		stock = Stock('TIME_SERIES_INTRADAY', ticker, 1, 1) # random args
		watchlist_tickers = Ticker.objects.filter(ticker__iexact=ticker, user=self.user)
		if not stock.is_valid():
			raise forms.ValidationError('Ticker ' + ticker + ' does not exist.')
		if watchlist_tickers.exists(): 
			raise forms.ValidationError('Ticker ' + ticker + ' is already on your watch list.')
		return ticker





