from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
class SignupDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
class CartDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Products=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Total_Price=models.IntegerField(null=True,blank=True)
    Prod_Image=models.ImageField(upload_to="Cart Images",null=True,blank=True)
class OrderDB(models. Model):
    Name = models. CharField(max_length=100, null=True, blank=True)
    Email = models. EmailField(max_length=100, null=True, blank=True)
    Place = models. CharField(max_length=100, null=True, blank=True)
    Address = models. CharField(max_length=100, null=True, blank=True)
    Mobile = models. CharField(max_length=100,null=True,blank=True)
    State = models. CharField(max_length=100, null=True, blank=True)
    Pin = models. CharField(max_length=100,null=True, blank=True)
    TotalPrice = models. IntegerField(null=True, blank=True)
    Message = models. CharField(max_length=100, null=True, blank=True)