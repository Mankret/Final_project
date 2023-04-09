from django.contrib.auth.models import User
from django.db import models
#from warehouse.warehouse_api.models import Book as WarehouseBook


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    summary = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    #id_in_warehouse = models.ForeignKey(WarehouseBook, on_delete=models.SET_NULL, null=True)



class Order(models.Model):
    STATUS_CHOICE = (
        ('cart', 'Cart'),
        ('ordered', 'Ordered'),
        ('success','Success'),
        ('Fail', 'fail'),
    )

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=10)
    delivery_adress = models.CharField(max_length=320)

class OrderItem(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    book_warehouse_id = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()