from django.db import models
from django.db.models import QuerySet,Sum,F,ExpressionWrapper,FloatField
from django.contrib.auth.models import User
from product.models import product
# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    def __str__(self):
        return self.user.username
    def cart_total_amount(self):
        cart_total_amount= self.cartitem_set.annotate(
            numeric_quantity=ExpressionWrapper(F('quantity'), output_field=FloatField())
        ).aggregate(
            cart_total_amount=Sum(F('product__price') * F('numeric_quantity'))
        )['cart_total_amount']
        return cart_total_amount
        

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=20)
    def __str__(self):
        return self.product.name
    def numeric_quantity(self):
        quantity=int(self.quantity)
        return quantity