# Generated by Django 5.1.3 on 2024-11-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_product_bahan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nama Produk'),
        ),
    ]