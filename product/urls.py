from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist/<str:pk>', views.wishlist_add, name="addwishlist"),
]
