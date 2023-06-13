from django.shortcuts import render
from .models import SubCategory
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from product.forms import ProductsForm,UserRegisterForm,UserProfileForm,ReviewForm
from product.models import product,Reviews
from Estimate.forms import EstimateForm
from django.contrib.auth import authenticate,login,logout
from category.models import Category
from django.db.models import Q
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def subCategoryView(request,id):
    category=SubCategory.objects.filter(category=id)
    return render(request,'subCategory.html',{'category':category}) 

def productcatev(request,id):
    data=product.objects.filter(category_name=id)
    data1= Category.objects.filter(status=True)
    p = Paginator(data, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'data1':data1,
        'page_obj':page_obj
    }
    return render(request,"shopcate.html",context)