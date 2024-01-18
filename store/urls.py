# from django.contrib import admin
# from django.urls import path
# from store import views

# urlpatterns = [
    
# ]
# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.product_list, name='product_list'),  
    path('store/', views.add_to_cart, name='add_to_cart'),  
    path('store/', views.view_cart, name='view_cart'),  
    path('store/', views.checkout, name='checkout'),  
]
