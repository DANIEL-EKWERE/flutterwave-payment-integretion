from django.contrib import admin
from .models import Product,ProductFormModel
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductFormModel)