from django.contrib import admin
from product.models import Product ,Category ,ShopDetail


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   prepopulated_fields = {
       'slug': ['name']
   }

   list_display = ['name', 'price', 'in_stock', 'is_active', 'quantity']
   list_filter = ['price', 'in_stock', 'is_active', 'quantity']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name']
    }

admin.site.register(ShopDetail)