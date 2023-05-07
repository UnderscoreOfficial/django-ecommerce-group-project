from django.urls import path

from . import views

urlpatterns = [
    path(f'product/<int:id>/', views.productDetails, name="productDetailShort"),
    path(f'product/<int:id>/<slug:name>/', views.productDetails, name="productDetail")
]
