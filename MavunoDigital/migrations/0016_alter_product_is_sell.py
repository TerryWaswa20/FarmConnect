# Generated by Django 4.2.7 on 2024-03-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MavunoDigital', '0015_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_sell',
            field=models.BooleanField(default=True),
        ),
    ]