# Generated by Django 4.2 on 2023-04-11 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_id',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
