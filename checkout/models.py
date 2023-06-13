from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CheckOut(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    checkout_email = models.EmailField()
    address = models.TextField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20,choices=(
        ('GJ','Gujarat'),
        ('Delhi','Delhi')
    ))
    product_qty = models.FloatField()
    products_id = models.CharField(max_length=50)
    Payment_status = models.CharField(max_length=10,choices=(
        ('Paid','Paid'),
        ('Pending','Pending')
    ))
    OrderPrice=models.CharField(max_length=20)
    checkout_date =models.DateField(_("date Created"), default=timezone.now)

    def __str__(self):
        return self.first_name