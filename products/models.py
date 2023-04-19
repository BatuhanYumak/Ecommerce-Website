from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_photo = models.ImageField(upload_to='product_photo/', null=True, blank=True)
