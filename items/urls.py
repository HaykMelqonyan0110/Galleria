from django.urls import path
from .views import home, category_detail, subcategory_detail, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('subcategory/<int:pk>/', subcategory_detail, name='subcategory_detail'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]
