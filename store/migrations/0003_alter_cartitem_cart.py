# Generated by Django 5.0.6 on 2024-09-12 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_cartitem_price_alter_cartitem_qauntity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cart_detail', to='store.cart'),
        ),
    ]
