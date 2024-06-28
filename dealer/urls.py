from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('dealerlogin/', views.dealerlogin, name='dealerlogin'),
    path('dealersignin/', views.dealersignin, name='dealersignin'),
    path('dforgetpage/', views.dforgetpage, name='dforgetpage'),
    path('createduser/', views.creatduser, name='createduser'),
    path('checkdlogin/', views.checkdlogin, name='checkdlogin'),
    path('dforgetpassword/', views.dforgetpassword, name='dforgetpassword'),
    path('dmenu/', views.menu, name='dmenu'),
    path('add/', views.add, name='add'),
    path('additem/', views.additem, name='additem')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)