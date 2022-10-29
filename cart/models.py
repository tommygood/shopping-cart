from django.db import models
from django.contrib import admin

class users(models.Model) :
    no = models.AutoField(primary_key=True)
    pwd = models.IntegerField(blank=True, null=True) # 密碼
    title = models.CharField(max_length = 10, blank=True, null=True) # 密碼

class product(models.Model) :
    no = models.AutoField(primary_key=True)
    pwd = models.IntegerField(blank=True, null=True) # 密碼
    name = models.CharField(max_length = 15, blank=True, null=True) # 密碼
    price = models.IntegerField(blank=True, null=True) # 密碼
    stock = models.IntegerField(blank=True, null=True) # 密碼

class shop_cart(models.Model) :
    no = models.AutoField(primary_key=True)
    uId = models.IntegerField(blank=True, null=True) # 密碼
    pId = models.IntegerField(blank=True, null=True) # 密碼
    amount = models.IntegerField(blank=True, null=True) # 密碼
    paid = models.IntegerField(default = 1, blank=False, null=True) # 密碼
    delivered = models.IntegerField(default = 1, blank=True, null=True) # 密碼
