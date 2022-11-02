from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="static/profiles",default="static/profiles/ab01437a16fdf57072342eb1a9bc303a.jpg")
    email = models.CharField(max_length=200,null=True)
    phonenumber = models.CharField(max_length=200,null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return  self.name

class Product(models.Model):
    category = (
        ('indoor','In door'),
        ('outdoor','Out door')
    )
    productsName = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=category)
    description = models.CharField(max_length=200,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True) 
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.productsName
class Order(models.Model):
    status = (
        ('pending','Pending'),
        ('out for delivery','Out For Delivery'),
        ('delivered','Delivered')
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=status)

    def __str__(self):
        return self.product.productsName