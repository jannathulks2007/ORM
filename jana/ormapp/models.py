from django.db import models

# Create your models here.
from django.contrib import admin
class Customer(models.Model):
    Product=models.CharField(max_length=100)
    Manufacture_part_Number=models.CharField(max_length=10,primary_key="True")
    Manufacturing_Date=models.DateField()
    Expiry_Date=models.DateField()
    Price=models.FloatField()
    Quantity=models.CharField(max_length=5)
    Ingredients=models.TextField()
class ProductAdmin(admin.ModelAdmin):
    list_display=["Product","Manufacture_part_Number","Manufacturing_Date","Expiry_Date","Price","Quantity","Ingredients"]