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

	def clean(self):
		cleaned_data = super().clean()
		time_series = cleaned_data.get('time_series')
		interval = cleaned_data.get('interval')
		if time_series == 'Intraday' and interval is None:
			raise forms.ValidationError('Please enter an interval to go along with intraday time series.')
		return self.cleaned_data

	def clean_ticker(self):
		ticker = self.cleaned_data['ticker']
		stock = Stock(function='Intraday', symbol=ticker, interval=5) # random args
		watchlist_tickers = Ticker.objects.filter(ticker__iexact=ticker, user=self.user)
		if not stock.is_valid():
			raise forms.ValidationError('Ticker ' + ticker + ' does not exist.')
		if watchlist_tickers.exists(): 
			raise forms.ValidationError('Ticker ' + ticker + ' is already on your watch list.')
		return ticker.upper()


# make sure interval exists if intraday selected otherwise Nonemin shows up

		




