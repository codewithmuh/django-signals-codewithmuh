from django.db import models

# Create your models here.

class User(models.Model):
    
    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', "Female"),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=4, choices= GENDER_CHOICES)

class Product(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()


class Statistics(models.Model):
    total_orders = models.PositiveIntegerField(default=0)