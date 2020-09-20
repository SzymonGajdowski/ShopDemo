from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(default='products_images/default.jpg', upload_to='products_images', null=True, blank=True)

    def __str__(self):
        return self.name
