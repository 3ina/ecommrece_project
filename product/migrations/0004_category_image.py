# Generated by Django 4.2.5 on 2023-09-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/default.png', null=True, upload_to='category/'),
        ),
    ]
