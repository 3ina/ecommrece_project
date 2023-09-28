from django.shortcuts import render
from cart.cart import Cart
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required



@require_POST
def add_to_cart(request,slug):
    pass



