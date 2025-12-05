from django.shortcuts import redirect, render
from .models import Product, Product_Purchase
from accounts.models import Address
# Create your views here.
def home(request):
    
    products = Product.objects.all()
    return render(request,'index.html', {'products': products,})

def all_products(request):
    products = Product.objects.all()
    return render(request,'all_products.html', {'products': products, 'user':request.user})
def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'product': product, 'user':request.user})

def purchase_product(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            full_name = request.POST['full_name']
            phone = request.POST['phone']
            pincode = request.POST['pincode']
            locality = request.POST['locality']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            landmark = request.POST['landmark']
            address =Address.objects.create(
                User = user,
                full_name = full_name,
                phone = phone,
                pincode = pincode,
                locality = locality,
                address = address,
                city = city,
                state = state,
                landmark = landmark
            )
            address.save()
            puchase_data = Product_Purchase.objects.create(
                ADDRESS = address,
                PRODUCT = product,
                quantity = 1,
                total_price = product.price,
                status = 'pending')
            puchase_data.save()
            return redirect('all_products')
    else:
        return redirect('register')
    return render(request,'address.html')

def my_orders(request):
    if request.user.is_authenticated:
        user = request.user
        orders = Product_Purchase.objects.filter(ADDRESS__User=user).order_by('-purchase_date')
        return render(request, 'orders.html',{'orders': orders})
    else:
        return redirect('home')