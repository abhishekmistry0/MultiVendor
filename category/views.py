from django.shortcuts import render
from .models import SubCategory
# Create your views here.
def subCategoryView(request,id):
    category=SubCategory.objects.filter(category=id)
    return render(request,'category.html',{'category':category}) 