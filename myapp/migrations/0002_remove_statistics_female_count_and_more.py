# Generated by Django 4.2.3 on 2023-07-23 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='female_count',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='male_count',
        ),
    ]