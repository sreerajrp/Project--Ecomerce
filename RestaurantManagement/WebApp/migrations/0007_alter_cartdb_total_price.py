# Generated by Django 5.1.3 on 2025-02-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_orderdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdb',
            name='Total_Price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
