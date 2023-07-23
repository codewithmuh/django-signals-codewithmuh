from django.contrib import admin
from .models import User, Product, Statistics, Order
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Order)    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',  'product', 'order_date')


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('total_orders', 'male_count', 'female_count')
    