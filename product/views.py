from django.shortcuts import render ,get_object_or_404
from product.models import Product,Category
from django.views import generic

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products' : products,
        'categories' : categories
    }
    return render(request,'product/index.html',context)


def detail(request,slug):
    product = get_object_or_404(Product,slug=slug)
    products = Product.objects.filter(category=product.category)
    context = {
        "product" : product,
        "products" : products
    }
    return  render(request,"product/detail.html",context)


