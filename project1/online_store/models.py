from django.db import models
from django.contrib.auth.models import User
class product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    activity=models.TextField()
    dates=models.TextField()
    months=models.TextField()
    hours=models.TextField()
    mins=models.TextField(default="00")
    years=models.TextField(default="2023")
class add_item_done(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    activity=models.TextField()
    dates=models.TextField()
    months=models.TextField()
    hours=models.TextField()
    mins=models.TextField(default="00")
    years=models.TextField(default="2023")
class rate_us(models.Model):
    rating=models.TextField()
    description=models.TextField()

