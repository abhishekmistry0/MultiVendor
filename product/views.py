from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ProductsForm,UserRegisterForm,UserProfileForm,ReviewForm
from .models import product,Reviews
from Estimate.forms import EstimateForm
from django.contrib.auth import authenticate,login,logout
from category.models import Category
from cart.cart import Cart
from django.db.models import Q
from checkout.models import CheckOut
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('userlogin')

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



def main(request):
    data=Category.objects.filter(status=True)
    data1=product.objects.all()
    p = Paginator(data1, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context={
        'data':data,
        'page_obj': page_obj
    }
    return render(request,'main.html',context)


def shop(request):
    data=product.objects.all()
    data1= Category.objects.filter(status=True)
    p = Paginator(data,per_page=10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context={
        'data':data,
        'data1':data1,
        'page_obj':page_obj
    }
    return render(request,"shop.html",context)

# @login_required(login_url='userlogin')
# def cart(request):  
#     total =0.00000
#     cart = request.session.get('cart', None)
#     values= (list(cart.values()))
#     for i in values:
#         total+=float(i['price'])*float(i['quantity'])
#     return render(request,"cart.html",{'total':total})


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

def userregister(request):
    data = UserRegisterForm(request.POST)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('userlogin')
        else:
            return render(request,"register.html",{'data':data,'msg':data.errors})
    return render(request,'register.html',{'data':data})


def index(request):
    data = ProductsForm(request.POST,request.FILES)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('showdata')
        else:
            print("error")
    return render(request,"index.html",{'data':data})

def showdata(request):
    data = product.objects.all()
    return render(request,"showdata.html",{'data':data})

def userdeletedata(request,id):
    data = product.objects.get(id=id)
    if data:
        data.delete()
        return redirect('showdata')
    else:
        print("No Data Found")
    return render(request,"showdata.html")


@login_required(login_url='userlogin')
def userupdate(request,id):
    data1 = product.objects.get(id=id)
    data = ProductsForm(request.POST or None,request.FILES or None,instance=data1)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('showdata')
        else:
            print("Error")
    return render(request,"updatedata.html",{'data':data})

def userlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin:index')
            else:
                login(request,user)
                return redirect('mainpage')
        else:
            return render(request,"login.html",{'msg':"invalid username or password"})
    return render(request,"login.html")

@login_required(login_url='userlogin')
def userlogout(request):
    logout(request)
    return redirect("mainpage")   

# @login_required(login_url='userlogin')
def UserProfile(request):
    user=request.user
    data = UserProfileForm(request.POST or None,instance=user)
    
    if request.method == "POST":
        data = UserProfileForm(request.POST or None,request.FILES,instance=user)
        if data.is_valid():
            user=data.save()
            # user=data.save(commit=False)
            # image_file = request.FILES['imag']
            # file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
            # user.userprofile.image=file_name
            return redirect('mainpage')
        else:
            print("error")

    return render(request,"UserProfile.html",{'data':data})
@login_required(login_url='userlogin')
def UserOrder(request):
    data = CheckOut.objects.filter(username=request.user)
    return render(request,"UserOrder.html",{'data':data})

@login_required(login_url='userlogin')
def SerchProduct(request):
    data1 = Category.objects.filter(status=True)
    qdata = request.GET.get('q')
    data = product.objects.filter(
         Q(name__icontains=qdata) | Q(price__icontains=qdata))
    return render(request,"SearchProduct.html",{'data':data,'data1':data1})

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
    

def Aboutus(request):
    return render(request,"aboutus.html")
