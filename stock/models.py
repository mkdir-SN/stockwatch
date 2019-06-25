from django import forms
from django.conf import settings
from django.db import models
from django.forms import ModelForm 
from django.contrib.auth.models import User


class Ticker(models.Model):
	INTERVAL_CHOICES = [
		(1, '1'),
		(5, '5'),
		(15, '15'),
		(30, '30'),
		(60, '60')
	]

	INTRADAY = 'INTRADAY'
	DAILY = 'DAILY'
	WEEKLY = 'WEEKLY'
	MONTHLY = 'MONTHLY'


	TIME_SERIES_CHOICES = [
		(INTRADAY, 'Intraday'),
		(DAILY, 'Daily'),
		(WEEKLY, 'Weekly'),
		(MONTHLY, 'Monthly')
	]

	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	ticker = models.CharField(max_length=10, blank=False) 
	time_series = models.CharField(max_length=20, choices=TIME_SERIES_CHOICES, default=MONTHLY)
	interval = models.IntegerField(choices=INTERVAL_CHOICES, default=30)

class History(models.Model): # if stock bought or sold
	ticker = models.ForeignKey(Ticker, on_delete=models.PROTECT) # raise error on deletion of Ticker with History objects associated with it
	open_price = models.IntegerField(blank=False, null=False)
	high_price = models.IntegerField(blank=False, null=False)
	low_price = models.IntegerField(blank=False, null=False)
	close_price = models.IntegerField(blank=False, null=False)
	volume_price = models.IntegerField(blank=False, null=False)
	amount_bought = models.IntegerField(blank=False, null=False)
	amount_spent = models.IntegerField(blank=False, null=False)
	time_bought = models.IntegerField(blank=True, null=True)
	time_sold = models.IntegerField(blank=True, null=True)
