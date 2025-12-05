from django.db import models

# Create your models here.
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    cart_id = models.CharField(max_length=250, unique=True)

class CartItem(models.Model):
    CART = models.ForeignKey(Cart, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return str(self.PRODUCT.name)
