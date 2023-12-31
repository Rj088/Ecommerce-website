# Generated by Django 4.2.3 on 2023-08-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_product_cat_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('1', 'Mobile'), ('2', 'Shoe'), ('3', 'Cloth')], max_length=10, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='product Name'),
        ),
    ]
