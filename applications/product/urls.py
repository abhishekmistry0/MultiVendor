from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.shop,name="shop"),
    path('shop/<str:whishlist>',views.shop,name="shop"),
    path('ProductDetails/<int:id>/',views.ProductDetails,name="ProductDetails"),
    path('whishlist/<int:id>/',views.WhishListView,name="WhishList"),
    path('search/suggestions/', views.SearchSuggestionView.as_view(), name='SearchSuggestions'),

]   