from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class Product(models.Model):
    size = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),

    )

    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    size = models.CharField(max_length=20,choices=size)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.name


class ShopDetail(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()