from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from stock.forms import TickerForm # model form
from stock.models import Ticker # model

@login_required
def addticker_view(request):
	form = TickerForm(request.POST)
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
	context = {'ticker_list': qs}
	return render(request, 'stock/watchlist.html', context)




