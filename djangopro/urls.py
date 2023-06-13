"""djangopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("mainUserInterface.urls")),
    path('product/',include("product.urls")),
    path('contactus/',include("contactus.urls")),
    path('checkout/',include("checkout.urls")),
    path('Estimate/',include("Estimate.urls")),
    path('category/',include("category.urls")),
    path('cart/',include("cart.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



admin.site.site_header = 'Multi Vendor'                    # default: "Django Administration"
admin.site.index_title = 'Multi Vendor'                 # default: "Site administration"
admin.site.site_title = 'Multi Vendor ' # default: "Django site admin"