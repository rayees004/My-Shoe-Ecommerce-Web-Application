from django.shortcuts import render,redirect
from shop.models import Product_Purchase

# Create your views here.
def home(request):
    return render(request,'admin.html')

def orderslist(request):
    orders = Product_Purchase.objects.filter(status='pending').order_by('purchase_date')
    return render(request,'orderslist.html',{'orders':orders})

def orderapprove(request,purchase_id):
    order = Product_Purchase.objects.get(id=purchase_id)
    order.status = 'order Approved'
    order.save()
    return redirect('orderslist')

def approvedlist(request):
    orders = Product_Purchase.objects.filter(status='order Approved').order_by('-purchase_date')
    return render(request,'approvedlist.html',{'orders':orders})

def orderreject(request,purchase_id):
    order = Product_Purchase.objects.get(id=purchase_id)
    order.status = 'rejected'
    order.save()
    return redirect('orderslist')

def rejectedlist(request):
    orders = Product_Purchase.objects.filter(status='rejected').order_by('-purchase_date')
    return render(request,'rejectedlist.html',{'orders':orders})

def allorderslist(request):
    orders = Product_Purchase.objects.all().order_by('-purchase_date')
    return render(request,'allorderslist.html',{'orders':orders})

def updatestatus(request,purchase_id):
    order = Product_Purchase.objects.get(id=purchase_id)
    if request.method == 'POST':
        status = request.POST['orders_status']
        order.status = status
        order.save()
        return redirect('allorderslist')
    return render(request,'updatestatus.html')


def delivedproduct(request):
    orders = Product_Purchase.objects.filter(status='Deliverd').order_by('-purchase_date')
    
    return render(request,'allorderslist.html',{'orders':orders})

