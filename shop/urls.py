from django.urls import path
from . import views
from accounts import views as account
from admininterface import views as admin

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('register/',account.register,name='register'),
    path('login/',account.login,name='login'),
    path('purchase/<int:product_id>/',views.purchase_product,name='purchase_product'),
    path('my_orders/',views.my_orders,name='my_orders'),
    path('adminhome/',admin.home,name='adminhome'),
    path('orderslist/',admin.orderslist,name='orderslist'),
    path('orderapprove/<int:purchase_id>/',admin.orderapprove,name='orderapprove'),
    path('orderrejection/<int:purchase_id>/',admin.orderreject,name='orderreject'),
    path('allorderslist/',admin.allorderslist,name='allorderslist'),
    path('approvedlist/',admin.approvedlist,name='approvedlist'),
    path('rejectedlist/',admin.rejectedlist,name='rejectedlist'),
    path('deliverdproduct/',admin.delivedproduct,name='deliverdproduct'),
    path('updatestatus/<int:purchase_id>/',admin.updatestatus,name='updatestatus'),
    path('search/',views.product_search,name='search'),
    path('listproduct/',admin.listproduct,name='listproduct'),
    path('productadd/',admin.addproduct,name='productadd'),
    path('editproduct/<int:product_id>/',admin.editproduct,name='editproduct'),
    path('removeproduct/<int:product_id>/',admin.removeproduct,name='removeproduct'),


    

]
