# Generated by Django 4.2.1 on 2023-05-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
