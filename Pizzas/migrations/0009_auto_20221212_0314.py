# Generated by Django 3.0.5 on 2022-12-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzas', '0008_auto_20221212_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='img', width_field=200),
        ),
    ]