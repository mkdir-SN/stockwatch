from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): 
			form.save()
			return redirect('/accounts/login') 
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'registration/register.html', context)

def home_view(request):
	return render(request, 'stockwatch/home.html')