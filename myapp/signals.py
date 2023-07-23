from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from .models import User, Order, Statistics

@receiver(pre_save, sender=Order)
def update_order_count(sender, instance, **kwargs):
    try:
        statistics = Statistics.objects.all().first()
    except Statistics.DoesNotExist:
        statistics = Statistics.objects.create()

    statistics.total_orders += 1 
    statistics.save()        

@receiver(post_delete, sender=Order)
def decrement_order_count(sender, instance, **kwargs):
    try:
        statistics = Statistics.objects.all().first()
    except Statistics.DoesNotExist:
        statistics = Statistics.objects.create()

    statistics.total_orders -= 1 
    statistics.save() 


    




 
 