from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    summary = models.TextField()
    price = models.DecimalField()


class BookItem(models.Model):
    book_id = models.OneToOneField("Book", on_delete=models.CASCADE)
    # place = ... maybe added ...

class Order(models.Model):
    user_email = models.EmailField()
    status = models.CharField()
    delivery_adress = models.CharField(max_length=320)
    # order_id_in_shop = models.OneToOneField() # app shop not create yet


class OrderItem(models.Model):
    order_id = models.OneToOneField("Order", on_delete=models.CASCADE)
    book_warehouse_id = models.OneToOneField("Book", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class OrderItemBookItem(models.Model):
    order_item_id = models.OneToOneField("Order", on_delete=models.CASCADE)
    book_item_id = models.OneToOneField("Book", on_delete=models.CASCADE)


