# Generated by Django 4.2 on 2023-04-11 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse_api', '0004_remove_bookitem_book_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('publication_year', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('in_work', 'In work'), ('success', 'Success'), ('Fail', 'fail')], max_length=10)),
                ('delivery_adress', models.CharField(max_length=320)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemBookItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_item_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='warehouse_api.book')),
                ('order_item_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='warehouse_api.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('book_warehouse_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='warehouse_api.book')),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='warehouse_api.order')),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='warehouse_api.book')),
            ],
        ),
    ]
