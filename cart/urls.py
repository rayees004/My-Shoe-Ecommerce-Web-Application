from django.urls import path,include
from .import views

urlpatterns = [
    path('minicart/<int:product_id>/',views.min_cart,name='min_cart'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart_details/',views.cart_details,name='cart_details'),
]