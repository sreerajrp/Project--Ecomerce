from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="images",null=True,blank=True)
class ProductDB(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Product_Name =models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Product_Image = models.ImageField(upload_to="images", null=True, blank=True)

class ServiceDB(models.Model):
    Service_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
