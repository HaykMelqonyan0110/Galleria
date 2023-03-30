from django.urls import path
from . import views
# from .views import ProfileDetails


urlpatterns = [
    path("", views.profile, name='profile'),
    path("account/", views.account_details, name='account'),
    path("account/edit/", views.edit_account_details, name='account_edit'),
    path('shopping_bag/', views.shopping_bag, name='shopping_bag'),
    path('shopping_bag/buy/', views.buy, name='buy'),
    path('shopping_bag/delete/<pk>/', views.delete_from_bag, name='delete-from_bag'),
    path('shopping_bag/clear/', views.clear, name='clear_shopping_bag')
]
