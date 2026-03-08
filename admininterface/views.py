from django.shortcuts import render,redirect
from shop.models import Product_Purchase,Product


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

def listproduct(request):
    products = Product.objects.all()
    return render(request,'listproducts.html', {'products': products})

def addproduct(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        stock = request.POST['stock']
        product = Product(name=name,price=price,description=description,image=image,stock=stock)
        product.save()
    return render(request,'productadd.html')

def editproduct(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        try:
            image = request.FILES['image']
        except:
            image = product.image
        stock = request.POST['stock']
        product.name=name
        product.price=price
        product.description=description
        product.image=image
        product.stock=stock
        product.save()
        return redirect('adminhome')
    return render(request,'productadd.html',{'product':product})

def removeproduct(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('listproduct')
