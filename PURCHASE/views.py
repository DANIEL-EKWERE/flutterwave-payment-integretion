from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from .forms import *

# Create your views here.


def purchaseStandalone(request):
    prod = Product.objects.get(active=True)
    if request.method=='POST':
        # form = ProductForm(request.POST)
        # if form.is_valid():
        #      form.save()
        #      name=  form.cleaned_data.get('name')
        #      email = form.cleaned_data.get('email')
        #      phone = form.cleaned_data.get('phone')
        #      form = ProductFormModel(orgName=name,email=email,phone=phone)
             
        #      context = {
        #         'name':name,
        #         'email':email,
        #         'phone':phone,
        #      }
        # Name = request.POST['name'],
        # Email = request.POST['email'],
        # Phone = request.POST['phone'],
        # form = ProductFormModel(orgName=Name,email=Email,phone=Phone)
        # # print(f'the email is {Email}')
        # form.save()
        return render(request, 'purchase-standalone.html',{"prod":prod})
    else:
        form = ProductFormModel()
    ctx={
        'prod':prod,
        # 'form':form
    }
    return render(request,
                  'purchase-standalone.html',
                  ctx)
    # print(f'the name is {prod.name}')
    


def Home(request):
    prod = Product.objects.all()
    context= {'prod':prod}
    return render(request,'home.html',context)



def confirm_payment(request):
    if request.method=='POST':
        Name = request.POST['name'],
        Email = request.POST['email'],
        Phone = request.POST['phone'],
        form = ProductFormModel(orgName=Name,email=Email,phone=Phone)
        # print(f'the email is {Email}')
        form.save()
        return redirect('/')