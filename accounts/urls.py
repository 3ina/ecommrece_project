from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/',views.profile,name="profile")
]