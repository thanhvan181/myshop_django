# Generated by Django 3.0.8 on 2020-08-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
