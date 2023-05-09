from django.shortcuts import render
from products.models import Product


def homepage(request):
    # temp can add pageinator or something else
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, 'app/app.html', context=context)
