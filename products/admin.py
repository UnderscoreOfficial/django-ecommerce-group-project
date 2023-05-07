from django.contrib import admin
from .forms import ProductForm
from .models import Product, Category, Tag

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ("name", "slug", "description", "sale", "price",
                    "image", "get_categories", "get_tags", "rating")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
