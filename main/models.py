from django.db import models


# Create your models here.
class Client(models.Model):
    """Клиент"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Заказ (Официант)"""

    order = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client"
    )
    food_name = models.CharField(max_length=250)
    food_count = models.IntegerField()

    def __str__(self):
        return self.order.name


STATUS = (
    ("Поступил заказ", "Поступил заказ"),
    ("Готовится", "Готовится"),
    ("Приготовлено", "Приготовлено"),
    ("Заказ отдан", "Заказ отдан"),
)


class Admin(models.Model):
    """Администрация"""

    status = models.CharField(
        max_length=200,
        choices=STATUS,
    )

    def __str__(self):
        return self.status


class Status(models.Model):
    ordered = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="ordering_id"
    )
    admin = models.ForeignKey(
        Admin, on_delete=models.CASCADE, related_name="administrator"
    )
    status = models.CharField(
        max_length=200, choices=STATUS, null=True, blank=True
    )

    def __str__(self):
        return self.admin
