# Generated by Django 5.0.1 on 2024-02-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]