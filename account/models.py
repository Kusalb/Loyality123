from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django import forms
from django.utils import timezone

# Create your models here.

class Waiter(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField()


class Partner(models.Model):
    Partner_company = models.CharField(max_length=250)
    Associted_person = models.CharField(max_length=250)
    email = models.EmailField()
    Phone_number = models.CharField(max_length=270)


class offer(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    offer_Name = models.CharField(max_length=250)
    Description = models.CharField(max_length=400)


class Discount(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    silver = models.CharField(max_length=250, default='')
    gold = models.CharField(max_length=250, default='')
    platinum = models.CharField(max_length=250, default='')
    # level1 = models.IntegerField(default=0)
    # level2 = models.IntegerField(default=0)
    # level3 = models.IntegerField(default=0)
    # discount_per= models.IntegerField(default=0)


class Customer(models.Model):
    engine_no = models.CharField(max_length=200,default='', null=False)
    chasis_no = models.CharField(max_length=200,default='', null=False)
    phone_no = models.CharField(max_length=15, default='', null=False)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200, default='')
    dob = models.DateField
    email = models.EmailField(max_length=100, default='')


class Promotion(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    Valid_till = models.DateField()
    Approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_image', default='')
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.Partner.Partner_company


class Trasaction(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    Discount = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)


# for creating superadmin

# class Superadmin(models.Model):
#     Username = models.CharField(max_length=100)
#     Email = models.EmailField()
#     password = models.CharField(max_length=100)


# for creating vespa admin

# class Vespaadmnin(models.Model):
#     Username = models.CharField(max_length=100)
#     Email = models.EmailField()
#     password = models.CharField(max_length=100)

class UserId(models.Model):
    engine_no = models.CharField(max_length=200, default='', null=False)
    first_name = models.CharField(max_length=50, default='')


    def __str__(self):
        return self.engine_no + "-" + self.first_name



class CustomUser(AbstractUser):
    is_Superadmin = models.BooleanField('Superadmin status', default=False)
    is_Vespadmin = models.BooleanField('Vespaadmin status', default=False)
    is_Partner = models.BooleanField('Partner status', default=False)
    is_Waiter = models.BooleanField('Waiter status', default=False)
    is_Customer = models.BooleanField('Customer status', default=False)
    Username = models.CharField(max_length=200, default='')
    Password = models.CharField(max_length=200, default='')


    def __str__(self):
        return self.email

