from django.shortcuts import render , get_object_or_404 ,redirect
from cart.cart import Cart
from product.models import Product
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from cart.forms import AddToCartForm
from django.contrib import messages



@login_required
@require_POST
def add_to_cart(request,slug):
    cart = Cart(request)
    product = get_object_or_404(Product,slug=slug)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        if not cart.product_exists(product):
            cd = form.cleaned_data
            if cd['quantity'] > product.quantity:
                messages.error(request,"The selected number is not allowed")
                return redirect('product:detail',slug=product.slug)

            cart.add(product,quantity=cd['quantity'])
            messages.success(request,"Added to cart")
            return redirect('product:detail', slug=product.slug)
        else:
            cd = form.cleaned_data
            if cd['quantity'] > product.quantity:
                messages.error(request, "The selected number is not allowed")
                return redirect('product:detail', slug=product.slug)

            cart.add(product, quantity=cd['quantity'],update_quantity=True)
            messages.success(request, "The card has been updated")
            return redirect('product:detail', slug=product.slug)




@login_required
def delete_form_cart(request,slug):
    cart = Cart(request)
    product = get_object_or_404(Product,slug=slug)
    cart.remove(product)
    return redirect('cart:cart-detail')


@login_required
def cart_detail(request):

    cart = Cart(request)
    context = {
        'cart' : cart
    }

    return render(request,'cart/cart_detail.html',context)



