from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepageView,name="HomePage"),
    path("adduser/",views.adduserView,name="adduser"),
    path("adduser/<str:adduser>/",views.adduserView,name="adduser"),
    path("adduser/<int:relativeId>/",views.adduserView,name="adduser"),
    path("registercar/",views.registercarView,name="registercar"),
]