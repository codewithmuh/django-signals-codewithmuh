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

@receiver(pre_delete, sender=Order)
def decrement_gender_count(sender, instance, **kwargs):
    try:
        statistics = Statistics.objects.all().first()
    except Statistics.DoesNotExist:
        statistics = Statistics.objects.create()

    if instance.customer.gender == 'M':
        statistics.male_count -= 1
    elif instance.customer.gender == 'F':
        statistics.female_count -= 1
    statistics.save()

@receiver(post_save, sender=User)
def update_customer_gender_count(sender, instance, created, **kwargs):
    try:
        statistics = Statistics.objects.all().first()
    except Statistics.DoesNotExist:
        statistics = Statistics.objects.create()

    if created:
        if instance.gender == 'M':
            statistics.male_count += 1
        elif instance.gender == 'F':
            statistics.female_count += 1
    statistics.save()
