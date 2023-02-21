from django.db import models

# Create your models here.
class Admindb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Profile")
class Addcategorydb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile")
class Productdetailsdb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile", null=True, blank=True)
