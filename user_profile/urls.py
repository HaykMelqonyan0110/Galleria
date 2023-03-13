from django.urls import path
from . import views
from .views import ProfileDetails


urlpatterns = [
    path("", views.profile, name='profile'),
    path("account/", views.account_details, name='account'),
    path("account/edit/", ProfileDetails.as_view(), name='account_edit'),
    path("account/returns/", views.returns, name='returns'),
]
