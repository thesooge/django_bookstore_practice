# Generated by Django 5.0.6 on 2024-07-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_bookmodel_description_alter_bookmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(blank=True, upload_to='media/book_cover/'),
        ),
    ]
