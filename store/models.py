from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    class Meta:
        app_label = 'store'
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null = True, blank = True)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null = True, blank = True)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits = 10,decimal_places=2)
    created_at = models.DateField(auto_now_add=True)