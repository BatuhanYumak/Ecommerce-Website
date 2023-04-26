from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    
