# Generated by Django 4.2 on 2023-04-10 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='book_warehouse_id',
            new_name='book_id',
        ),
    ]
