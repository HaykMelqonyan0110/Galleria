from django.urls import path
from . import views
from user_profile import views as profile_views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('shop_sub/<str:subcategory>/', views.subcategory_shop_view, name="only_subcategory"),
    path('shop/men/', views.men_shop_view, name='shop_men'),
    path('shop/men/<str:subcategory>/', views.men_sub_shop_view, name='shop_men_sub'),
    path('shop/women/', views.women_shop_view, name='shop_women'),
    path('shop/women/<str:subcategory>/', views.women_sub_shop_view, name='shop_women_sub'),
    path('shop/kids/', views.kids_shop_view, name='shop_kids'),
    path('shop/kids/<str:subcategory>/', views.kids_sub_shop_view, name='shop_kids_sub'),
    path('shop/<pk>/', views.ItemView.as_view(), name='item_view'),
    path('shop/<pk>/added/', profile_views.add_to_shopping_bag, name='add_to_shopping_bag')

]
