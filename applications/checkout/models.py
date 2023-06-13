from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class CheckOut(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    checkout_email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20, choices=(
        ('GJ', 'Gujarat'),
        ('Delhi', 'DH')
    ))
    Payment_status = models.CharField(max_length=10, choices=(
        ('Paid', 'Paid'),
        ('Pending', 'Pending')
    ))
    totalOrderPrice = models.CharField(max_length=20)
    checkout_date = models.DateField(
        'expiration time (of ad)', default=timezone.now() + datetime.timedelta(days=0))
    
    def __str__(self):
        return self.first_name


class OrdersItems(models.Model):
    order = models.ForeignKey(CheckOut,on_delete=models.PROTECT)
    ordersItem=models.ForeignKey('product.product',on_delete=models.CASCADE)
    orderedItemQuantity=models.CharField(max_length=20)
    def __str__(self):
        return self.ordersItem.name
    
