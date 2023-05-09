from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('cart/add/', views.cartAdd, name="cartAdd"),
    path('cart/remove/', views.cartRemove, name="cartRemove")
]
