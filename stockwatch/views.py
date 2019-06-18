from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): 
			form.save()
			return redirect('/accounts/login') # what happens if form is not valid?
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'stockwatch/register.html', context)