from django.db import models
from django import forms
from stock.models import Ticker
from stock.stock import apikey, get_data, Stock

class TickerForm(forms.ModelForm): 

	class Meta:
		model = Ticker
		fields = ['ticker', 'time_series', 'interval']

	def __init__(self, *args, **kwargs): # override init to access request.user from stock.views
         self.user = kwargs.pop('user')
         super(TickerForm, self).__init__(*args, **kwargs)

	def clean_ticker(self):
		ticker = self.cleaned_data['ticker']
		stock = Stock('intraday', ticker, 1, 1) # random args
		watchlist_tickers = Ticker.objects.filter(ticker__iexact=ticker, user=self.user)
		if not stock.is_valid():
			raise forms.ValidationError('Ticker ' + ticker + ' does not exist.')
		if watchlist_tickers.exists(): 
			raise forms.ValidationError('Ticker ' + ticker + ' is already on your watch list.')
		return ticker.upper()

	def clean_time_series(self):
		time_series = ticker = self.cleaned_data['time_series']
		return time_series.upper()







