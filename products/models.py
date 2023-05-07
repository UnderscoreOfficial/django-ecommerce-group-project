from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField(max_length=500)
    sale = models.PositiveBigIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, upload_to="products")
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    rating = models.PositiveBigIntegerField(
        default=0, validators=[MaxValueValidator(10)])

    @property
    def get_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])

    @property
    def get_categories(self):
        return ", ".join([tag.name for tag in self.tags.all()])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
