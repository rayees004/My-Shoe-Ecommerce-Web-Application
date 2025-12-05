from django.db import models
from accounts.models import Address

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 

class Product_Purchase(models.Model):
    ADDRESS = models.ForeignKey(Address,on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product,on_delete=models.CASCADE) 
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')