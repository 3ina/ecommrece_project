from django.shortcuts import render
from product.models import Product,Category

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products' : products,
        'categories' : categories
    }
    return render(request,'product/index.html',context)
