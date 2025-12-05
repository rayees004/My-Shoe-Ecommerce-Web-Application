from django.urls import path
from . import views
from accounts import views as account

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('register/',account.register,name='register'),
    path('login/',account.login,name='login'),
    path('purchase/<int:product_id>/',views.purchase_product,name='purchase_product'),
    path('my_orders/',views.my_orders,name='my_orders'),
]
