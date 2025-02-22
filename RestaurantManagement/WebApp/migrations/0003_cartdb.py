# Generated by Django 5.1.4 on 2025-01-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_signupdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Products', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Total_Price', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Prod_Image', models.ImageField(blank=True, null=True, upload_to='Cart Images')),
            ],
        ),
    ]
