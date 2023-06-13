from django.urls import  path
from . import views

urlpatterns=[
    path('<int:id>/',views.subCategoryView,name='subCategory'),
    path('productcatev/<int:id>/',views.productcatev,name="productcatev"),
]