from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render ,get_object_or_404
from product.models import Product,Category
from django.views import generic
from product.forms import Contact

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


def shop(request,):
    products = Product.objects.all()


    context = {
        "products" : products
    }
    return render(request,'product/shop.html',context)


class ListCategory(generic.ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'product/categories.html'


def send_email(request):

    if request.method == "GET":
        form = Contact()
        return render(request,'product/contact.html',{"form" : form})

    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['firstname']
            lname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            text =  f"""
                    first name : {fname}
                    last name : {lname}
                    email : {email}
                    message : {message}
            """
            print(fname)
            #send_mail(f"{subject}", text, "3inaroydl@gmail.com", ("dentalapp109@gmail.com",))
            messages.success(request, "your message is send , we will call you soon")
            return render(request, 'product/email_sending.html')
        else:
            messages.error(request, "message doesn't send ")
            return render(request, 'product/email_sending.html')





def about(request):

    render(request,'product/about.html')