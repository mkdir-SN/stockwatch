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

	INTRADAY = 'Intraday'
	DAILY = 'Daily'
	WEEKLY = 'Weekly'
	MONTHLY = 'Monthly'


	TIME_SERIES_CHOICES = [
		(INTRADAY, 'Intraday'),
		(DAILY, 'Daily'),
		(WEEKLY, 'Weekly'),
		(MONTHLY, 'Monthly')
	]

	user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
	ticker = models.CharField(max_length=10) 
	time_series = models.CharField(max_length=20, choices=TIME_SERIES_CHOICES)
	interval = models.IntegerField(choices=INTERVAL_CHOICES, null=True, blank=True)
