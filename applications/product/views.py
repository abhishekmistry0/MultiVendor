from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from .forms import ProductsForm,UserRegisterForm,UserProfileForm,ReviewForm
from .models import product,Reviews,Whishlist
from Estimate.forms import EstimateForm
from django.contrib.auth import authenticate,login,logout
from category.models import Category
# from cart.cart import Cart
from django.db.models import Q,F
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views import View




def shop(request,whishlist=None):
    data=product.objects.all()
    data1= Category.objects.filter(status=True)
    if whishlist:
        whishlist = Whishlist.objects.filter(user=request.user).select_related('product')
        data = [item.product for item in whishlist]

    p = Paginator(data,per_page=10)
    page_number = request.GET.get('page')
    try:
        whishList=Whishlist.objects.filter(user=request.user)
    except:
        whishList=None
    # dataada=list(whishList)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context={
        'data':data,
        'data1':data1,
        'page_obj':page_obj,
        'whishList':whishList
    }
    return render(request,"shop.html",context)

def ProductDetails(request,id):
    data = product.objects.filter(id=id)
    data1 = ReviewForm(request.POST)
    data2=Reviews.objects.filter(product_review=id)
    if request.method == "POST":
        if data1.is_valid():
            model1=data1.save(commit=False)
            model1.product_review_id=id
            model1.save()
            return HttpResponseRedirect(request.path_info)
        else:
           return render(request,"ProductDetails.html",{'msg':data1.errors})
    p = Paginator(data2, 4)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    
    return render(request,"ProductDetails.html",{'data':data,'data1':data1,'data2':data2,'page_obj': page_obj})
    
def WhishListView(request,id):
    try:
        productObj=product.objects.get(id=id)
        whishlistObj=Whishlist.objects.get(
            user=request.user,
            product=productObj
        )
        whishlistObj.delete()

    except:
        productObj=product.objects.get(id=id)
        whishlistObj=Whishlist.objects.create(
            user=request.user,
            product=productObj
        )
        whishlistObj.save()
    return redirect(request.META.get('HTTP_REFERER'))

def whishList(request):
    user=request.user
    whishlistItemsCount=0
    if user.is_authenticated:
        whishlistItemsCount=Whishlist.objects.filter(user=request.user).count()
    return {"whishlistItemsCount":whishlistItemsCount}

class SearchSuggestionView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        products = product.objects.filter(name__icontains=query)
        ids = [product.id for product in products]
        names = [product.name for product in products]
        return JsonResponse({'ids': ids,'names':names})