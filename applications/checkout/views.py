from django.shortcuts import render,redirect
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
from .models import CheckOut,OrdersItems
from cart.models import Cart,CartItem
from datetime import datetime
from django.db.models import Prefetch
# from cart import context_processor

# Create your views here.

@login_required(login_url='userlogin')
def CheckoutViews(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        # product_qty = request.POST['product_qty']
        # products_id = request.POST['products_id']

        paymentid = request.POST['paymentid']
        city = request.POST['city']
        state = request.POST['state']
        cart_total_amount=Cart.objects.get(user=request.user).cart_total_amount()
        if city!='Ahmedabad':
            totalOrderPrice+=100
        data = CheckOut.objects.create(first_name=fname,last_name=lname,checkout_email=email,address=address,Payment_status=paymentid,city=city,state=state,totalOrderPrice=cart_total_amount,username=request.user.username)
        cart_items=CartItem.objects.filter(cart__user=request.user)
        for cart_item in cart_items:
            checkout_products=OrdersItems()
            checkout_products.order=data
            checkout_products.ordersItem=cart_item.product
            checkout_products.orderedItemQuantity=cart_item.quantity
            checkout_products.save()
        if data:
            if paymentid == "COD":
                data.save()
                return redirect('invoice')
            else:
                data.save()
                return redirect('Payment')
    return render(request,"checkout.html")



def Payment(request):
    return render(request,"Payment.html")


def invoice(request):
    data = datetime.now() 
    context = {
        'data':data
    }
    cartMdlObj=(
        Cart.objects
        .prefetch_related('cartitem_set__product')
        .get(user=request.user)
                )
    orderMdlObj=CheckOut.objects.filter(username=request.user.username).latest('id')
    context["cart"]=cartMdlObj
    context["order"]=orderMdlObj
    return render(request,"invoice.html",context)

@login_required(login_url='userlogin')
def UserOrder(request):
    orders = CheckOut.objects.prefetch_related(Prefetch('ordersitems_set',queryset=OrdersItems.objects.select_related('ordersItem'))).filter(username=request.user)
    return render(request,"UserOrder.html",{'orders':orders})