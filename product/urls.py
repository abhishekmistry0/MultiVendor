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
    path('shop/',views.shop,name="shop"),
    path('productcatev/<int:id>/',views.productcatev,name="productcatev"),
    
    path('SerchProduct/',views.SerchProduct,name="SerchProduct"),
    path('ProductDetails/<int:id>/',views.ProductDetails,name="ProductDetails"),
    path('UserProfile/',views.UserProfile,name="UserProfile"),
    path('UserOrder/',views.UserOrder,name="UserOrder"),
    path('Aboutus/',views.Aboutus,name="Aboutus"),
    
    path('PasswordChangeView/',PasswordChangeView.as_view(template_name='changepassword.html'),name="changepassword"),

]   