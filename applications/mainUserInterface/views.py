from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ProductsForm,UserRegisterForm,UserProfileForm
from product.models import product
from Estimate.forms import EstimateForm
from django.contrib.auth import authenticate,login,logout
from category.models import Category
from django.db.models import Q
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView as pcw
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class PasswordChangeView(pcw):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('mainpage')

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


# @login_required(login_url='userlogin')
# def cart(request):  
#     return render(request,"cart.html")




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
        if data.is_valid():
            data.save()
            return redirect('mainpage')
        else:
            print("error")
    return render(request,"UserProfile.html",{'data':data})



# def cart_add(request, id):
#     cart = Cart(request)
#     Product = product.objects.get(id=id)
#     cart.add(product=Product)
#     return redirect("cart")

# def item_increment(request, id):
#     cart = Cart(request)
#     Product = product.objects.get(id=id)
#     cart.add(product=Product)   
#     return redirect("cart")

# def item_decrement(request, id):
#     cart = Cart(request)
#     Product = product.objects.get(id=id)
#     cart.decrement(product=Product)
#     return redirect("cart")


# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("mainpage")

# def item_clear(request, id):
#     cart = Cart(request)
    
    # Product = product.objects.get(id=id)
    # cart.remove(Product)
    # return redirect("cart")

# @login_required(login_url='userlogin')
def SerchProduct(request):
    data1 = Category.objects.filter(status=True)
    qdata = request.GET.get('q')
    data = product.objects.filter(
         Q(name__icontains=qdata) | Q(price__icontains=qdata))
    return render(request,"SearchProduct.html",{'data':data,'data1':data1})


    

def Aboutus(request):
    return render(request,"aboutus.html")