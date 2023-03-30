from django.urls import path
from . import views


urlpatterns = [
    path("add/", views.add_item, name='add_item'),
    path('<pk>/', views.OwnerItem.as_view(), name='owner_item'),
    path('<pk>/update/', views.ItemUpdate.as_view(), name='update_item'),
    path('<pk>/delete/', views.ItemDelete.as_view(), name='delete_item'),
]
