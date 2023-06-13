from django.shortcuts import render,redirect
from .models import Cart,CartItem
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from product.models import product
import json
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='userlogin')
def cartView(request):
    context={}
    if request.user.is_authenticated:
        cartMdlObj=(
            Cart.objects
            .prefetch_related('cartitem_set__product')
            .get(user=request.user)
                    )
        context["cart"]=cartMdlObj
    else:
        cart_json = request.COOKIES.get('cart')
        cart = json.loads(cart_json) if cart_json else {}

        context["cart"]=cart
    return render(request,'cart.html',context)
@login_required(login_url='userlogin')
def cart_add(request, id):
    item=product.objects.get(id=id)
    if request.user.is_authenticated:
        try:
            cart_item=CartItem.objects.filter(cart__user=request.user).get(product=item)
            cart_item.quantity=str(int(cart_item.quantity)+1)
            cart_item.save()
        except:
            cart=Cart.objects.get(user=request.user)
            cart_item=CartItem()
            cart_item.cart=cart
            cart_item.product=item
            cart_item.quantity='1'
            cart_item.save()
    # else:
        # user=User.objects.get(pk=11)
        # cartMdlObj=Cart()
        # cartMdlObj.user=user
        # cartItemMdlObj=CartItem()
        # cartItemMdlObj.cart=cartMdlObj
        # cartItemMdlObj.product=item
        # cartItemMdlObj.quantity
    return redirect("cart")
@login_required(login_url='userlogin')
def item_increment(request, id):
    item=product.objects.get(id=id)
    cart_item = CartItem.objects.filter(cart__user=request.user).get(product=item)
    cart_item.quantity=str(int(cart_item.quantity)+1)
    cart_item.save() 
    return redirect("cart")

@login_required(login_url='userlogin')
def item_decrement(request, id):
    item=product.objects.get(id=id)
    cart_item = CartItem.objects.filter(cart__user=request.user).get(product=item)
    cart_item.quantity=str(int(cart_item.quantity)-1)
    cart_item.save()
    return redirect("cart")
@login_required(login_url='userlogin')
def cart_clear(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    cart_items.delete()
    return redirect("mainpage")
@login_required(login_url='userlogin')
def item_clear(request, id):
    item=product.objects.get(id=id)
    cart_item = CartItem.objects.filter(product=item)
    cart_item.delete()
    return redirect("cart")

def cart(request):
    context={}
    # response={}
    if request.user.is_authenticated:
        try:
            Cart.objects.get(user=request.user)
        except:
            cartMdlObj=Cart()
            cartMdlObj.user=request.user
            cartMdlObj.save()
        cart=get_object_or_404(Cart,user=request.user)
        cartItemsCount=CartItem.objects.filter(cart=cart).aggregate(quantity=Sum("quantity"))
        if cartItemsCount['quantity']:
            context['cartItemsCount']=cartItemsCount['quantity']
        else:
            context['cartItemsCount']=0
    else:
    #     cart_json = request.COOKIES.get('cart')
    #     cart = {}
    #     if cart_json:
    #         cart = json.loads(cart_json)
    #     if not cart_json:
    #         cart_json = json.dumps(cart)
    #         response = HttpResponse()
    #         response.set_cookie('cart', cart_json)
    #         context['response']=response
    #     if cart.__len__()==0:
    #         context['cartItemsCount']=0
    #     else:
    #         context['cartItemsCount']=1
        context['cartItemsCount']=0

    return context