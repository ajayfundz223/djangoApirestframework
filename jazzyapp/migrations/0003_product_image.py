# Generated by Django 4.1.3 on 2023-07-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazzyapp', '0002_remove_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to=''),
        ),
    ]