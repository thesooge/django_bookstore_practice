# Generated by Django 5.0.6 on 2024-07-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
