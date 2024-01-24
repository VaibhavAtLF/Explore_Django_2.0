from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),  
    path('view_cart/', views.view_cart, name='view_cart'),  
    path('checkout/<int:id>', views.checkout, name='checkout'),  
]
