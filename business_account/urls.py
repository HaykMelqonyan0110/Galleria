from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_account_views, name='business_account'),
    path('register/', views.register_business_account_view, name='register_bs_account'),
    path('edit_business_account/', views.edit_business_account_view, name='edit_bs_account'),
    path('account_details/', views.business_profile_details_view, name='bs_account_details'),
    path('orders/', views.business_account_orders_view, name='bs_account_orders'),
    path('orders/delete/<pk>/', views.business_account_order_delete, name="bs_account_order_delete"),
]
