from django.shortcuts import render,redirect
from .models import UserRelatives,CarRegistration
from django.contrib.auth.decorators import login_required
from .forms import UserRelativeProfileForm,CarRegistrationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User


# Create your views here.

def homepageView(request):
    return render(request,"main.html")

@login_required(login_url='userlogin')
def adduserView(request,adduser=None):
    context={}
    relatives=UserRelatives.objects.filter(user=request.user)
    context["relatives"]=relatives
    #Add Relative
    if adduser=="adduser":
        relativeForm = UserRelativeProfileForm(request.POST or None,request.FILES)
        if request.method=="POST" and relativeForm.is_valid():
            relative=relativeForm.save(commit=False)
            relative.user=request.user
            relative.save()
            return redirect("HomePage")
        context["relativeForm"]=relativeForm
        context["Title"]="Add Your Relative"
        return render(request,"relativeprofile.html",context)
    #Edit relative
    if adduser:
        relative=UserRelatives.objects.get(id=adduser)
        # relative.userRelativeFirstName
        # relative.userRelativeLastName
        # relative.userRelativeEmail
        # relative.userRelativeImage
        relativeForm = UserRelativeProfileForm(request.POST or None,instance=relative)
        if request.method=="POST" and relativeForm.is_valid():
            relativeForm = UserRelativeProfileForm(request.POST or None,request.FILES,instance=relative)

            relative=relativeForm.save(commit=False)
            relative.user=request.user
            relative.save()
            return redirect("HomePage")
        context["relative"]=relative
        context["Title"]="Edit Your Relative"
        context["relativeForm"]=relativeForm
        return render(request,"relativeprofile.html",context)
    return render(request,"adduser.html",context)

@login_required(login_url="userlogin")
def registercarView(request):
    context={}
    carRegistration=None
    try:
        carRegistration=CarRegistration.objects.get(user=request.user)
        carRegistrationForm=CarRegistrationForm(instance=carRegistration)
        context["Title"]="Edit Your Car Details"
    except Exception as e:
        context["Title"]="Register Your Car"
        carRegistrationForm=CarRegistrationForm()
    if request.method=="POST":
        if carRegistration:
            carRegistrationForm=CarRegistrationForm(request.POST,instance=carRegistration)
        else:
            carRegistrationForm=CarRegistrationForm(request.POST)
            context["Title"]="Register Your Car First"
        if carRegistrationForm.is_valid():
            carRegistration=carRegistrationForm.save(commit=False)
            carRegistration.user=request.user
            carRegistration.save()
            return redirect("HomePage")
        else:
            context["msg"]=f"{carRegistrationForm.errors}"
            return render(request,"registerCar.html",context)
    context['carRegistrationForm']=carRegistrationForm
    return render(request,"registerCar.html",context)