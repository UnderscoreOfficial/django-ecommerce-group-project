from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def productDetails(request, id: int, name: str = None):
    product = get_object_or_404(Product, id=id)

    if (name == None):
        return redirect("productDetail", id=id, name=product.slug)

    related_products = Product.objects.filter(
        categories=1).exclude(id=id).order_by("?")[:4]

    context = {
        "product": product,
        "related_products": related_products
    }
    return render(request, 'products/product.html', context=context)
