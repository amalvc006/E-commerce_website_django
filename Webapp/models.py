from django.db import models

# Create your models here.
class Customerdetails(models.Model):
    Username=models.CharField(max_length=100, null=True, blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)
    Password=models.CharField(max_length=100, null=True, blank=True)
    ConfirmPassword=models.CharField(max_length=100, null=True, blank=True)

class CheckOutdetails(models.Model):
    Firstname=models.CharField(max_length=100, null=True, blank=True)
    Lastname=models.CharField(max_length=100, null=True, blank=True)
    Address=models.CharField(max_length=100, null=True, blank=True)
    City=models.CharField(max_length=100, null=True, blank=True)
    Postcode=models.IntegerField(null=True, blank=True)
    Phone=models.IntegerField(null=True, blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)

class Contactus(models.Model):
    Name=models.CharField(max_length=100, null=True, blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)
    Subject=models.CharField(max_length=100, null=True, blank=True)
    Message=models.CharField(max_length=100, null=True, blank=True)