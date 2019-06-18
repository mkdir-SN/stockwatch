from django.db import models
from django.forms import ModelForm
from stock.models import Ticker

"""
def stock_info(function, symbol, interval, size, apikey):
	url = "https://www.alphavantage.co/query?function="+ str(function) + "&symbol=" + str(symbol) + "&interval=" + str(interval) + "min&outputsize=" + str(size) + "&apikey=" + str(apikey)
	print(url)
	json_data = requests.get(url).json()
	return json_data

def stock_is_valid(json_data):
	if json_data[0] is "Meta Data": 
		return True
	return False
"""

# form that is bound to a particular model (Ticker), can access Ticker model's table data
class TickerForm(ModelForm): 
	class Meta:
		model = Ticker
		fields = ['ticker']



