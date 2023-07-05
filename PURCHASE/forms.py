from .models import *
from django import forms
from django.forms import ModelForm

class ProductForm(forms.ModelForm):
    class meta:
        model = ProductFormModel
        fields = [
            'orgName',
            'email',
            'phone',
        ]