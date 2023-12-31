# Generated by Django 4.2.4 on 2023-10-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0004_alter_productmodel_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_subcategorybranch', to='category.subcategorybranchmodel', verbose_name='Sub Category Branch'),
        ),
    ]
