from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ecommrece_project import settings
from product.views import index,send_email ,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name="about"),
    path('contact/',send_email,name="send-email"),
    path('products/',include('product.urls',namespace="product")),
    path('accounts/',include('allauth.urls')),
    path('', index, name="index"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
