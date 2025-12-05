from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    locality = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    landmark = models.CharField(max_length=200, blank=True, null=True)
