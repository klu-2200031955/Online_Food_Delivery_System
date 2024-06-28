from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('customerhome/', views.customerhome, name='customerhome'),
    path('customersignin/', views.customersignin, name='customersignin'),
    path('cforgetpage/', views.cforgetpage, name='cforgetpage'),
    path('createcuser/', views.createcuser, name='createcuser'),
    path('checkclogin/', views.checkclogin, name='checkclogin'),
    path('cforgetpassword/', views.cforgetpassword, name='cforgetpassword'),
    path('spaymentpage/', views.spaymentpage, name='spaymentpage'),
    path('npaymentpage/', views.npaymentpage, name='npaymentpage'),
]
