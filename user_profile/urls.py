from django.urls import path
from . import views


urlpatterns = [
    path("", views.profile, name='profile'),
    path("account/", views.account_details, name='account'),
    path("account/edit/", views.edit_account_details, name='account_edit'),
    path("account/returns/", views.returns, name='returns'),
]
