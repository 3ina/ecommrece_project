from django.urls import path
from cart import views

app_name = "cart"
urlpatterns = [
        path('add-to-cart/<slug:slug>/',views.add_to_cart,name="add-to-cart"),
        path('delete-from-cart/<slug:slug>/',views.delete_form_cart,name="delete-from-cart"),
        path('cart-detail/',views.cart_detail,name="cart-detail"),

]
