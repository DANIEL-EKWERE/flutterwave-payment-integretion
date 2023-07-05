from django.urls import path
from . import views

urlpatterns = [
# path('',views.Home, name='home'),
path('',views.purchaseStandalone, name='purchaseStandalone'),
path('confirm_payment',views.confirm_payment, name='add')
]