from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from stock.forms import apikey, get_data, Stock, TickerForm # model form
from stock.models import Ticker # model


@login_required
def addticker_view(request):
	form = TickerForm(request.POST, user=request.user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		return redirect('/watchlist')
	context = {'form': form}
	return render(request, 'stock/addticker.html', context)

@login_required
def watchlist_view(request):
	qs = Ticker.objects.filter(user=request.user)
	username = request.user.username
	stock_objs = [(Stock(function=q.time_series, symbol=q.ticker, interval=q.interval), q.pk) for q in qs]
	# Create an in-depth list of stock names and prices to access within template by index
	stock_name_and_prices = [(s.stock_symbol(), s.stock_info()[2], s.stock_times(), s.stock_prices(), pk) for s, pk in stock_objs]
	# Index: 1. stock symbol (string), 2. stock information (string), 3. stock times (list), 4. stock prices (dictionary), 5. ticker ID in DB (int)
	if request.method == "POST":
		# Handles deletion of rows in Ticker model based on user selection in template
	    items_to_delete = request.POST.getlist('delete') 
	    Ticker.objects.filter(pk__in=items_to_delete).delete()
	    return redirect('/watchlist')
	context = {'stock_name_and_prices': stock_name_and_prices, 'username': username}
	return render(request, 'stock/watchlist.html', context)







