# Generated by Django 5.1.3 on 2024-11-30 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bahan',
        ),
    ]
