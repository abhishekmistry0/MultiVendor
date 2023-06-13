from django.urls import path
from .views import PasswordChangeView
from . import views

urlpatterns = [
    path('',views.main,name="mainpage"),
    path('index/',views.index,name="indexpage"),
    path('showdata/',views.showdata,name="showdata"),
    path('userdeletedata/<int:id>/',views.userdeletedata,name="userdeletedata"),
    path('userupdate/<int:id>/',views.userupdate,name="userupdate"),
    path('userregister/',views.userregister,name="userregister"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    # path('cart', views.cart, name='cart'),
    path('Aboutus/',views.Aboutus,name="Aboutus"),
    # path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    # path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('SerchProduct/',views.SerchProduct,name="SerchProduct"),
    path('UserProfile/',views.UserProfile,name="UserProfile"),
    # path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='changepassword.html'),name="changepassword"),
    # path('cart_clear/',views.cart_clear,name="cart_clear")

]   