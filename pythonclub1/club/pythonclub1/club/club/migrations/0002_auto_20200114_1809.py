# Generated by Django 3.0.2 on 2020-01-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productdescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productprice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='typedescription',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]