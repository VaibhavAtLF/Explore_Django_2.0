from django.db import models

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
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
