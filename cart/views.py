from django.shortcuts import render, redirect
from products.models import Product
import urllib.parse
import json


def cart(request):

    context = {}

    if request.user.is_authenticated:
        print("auth")
    else:
        try:
            cart_items_data = json.loads(
                urllib.parse.unquote(request.COOKIES.get('cart_items')))
            print(cart_items_data)
        except TypeError:
            cart_items_data = []

        cart_items = []
        for item in cart_items_data:
            cart_items.append({
                "product": Product.objects.get(id=item["product_id"]),
                "quantity": item["quantity"]
            })
        context = {
            "cart_items": cart_items
        }
    print("hi")

    return render(request, 'cart/cart.html', context=context)


def cartAdd(request):
    if request.method == "POST":
        product = request.POST.get("product_id")
        quantity = request.POST.get("input_quantity")
        # Product.objects.get(id=product)

        print(product, quantity)

        return redirect("cart")


def cartRemove(request):
    if request.method == "POST":
        product = request.POST.get("product_id")
        quantity = request.POST.get("input_quantity")
        # Product.objects.get(id=product)

        print(product, quantity)

        return redirect("cart")
