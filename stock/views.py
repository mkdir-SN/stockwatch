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
	# access model's Stock object for each qs object and pass into template as context variable
	stock_objs = [Stock(function=q.time_series, symbol=q.ticker, interval=q.interval) for q in qs[:6]]
	stock_infos = [s.stock_info() for s in stock_objs]
	context = {'stock_infos': stock_infos}
	return render(request, 'stock/watchlist.html', context)








