from django.conf import settings
from django.db import models
from django.forms import ModelForm 
from django.contrib.auth.models import User


class Ticker(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	ticker = models.CharField(max_length=10, blank=False)
