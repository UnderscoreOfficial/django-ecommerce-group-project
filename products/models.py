from django.db import models

class Example(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(null=True, upload_to="products")

    def __str__(self):
        return self.name