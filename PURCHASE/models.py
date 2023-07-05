from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ProductFormModel(models.Model):
    orgName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()



class Product(models.Model):
    productForm = models.ForeignKey(ProductFormModel,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_image/%Y/%m/%d/', default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def Price(self):
        total_price = self.Product.price
        return total_price


