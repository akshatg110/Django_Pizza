# Generated by Django 3.0.8 on 2020-09-08 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_ordermodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='status',
        ),
    ]
