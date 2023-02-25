from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from user import views as reg
from user_profile import views as user_profile_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path("profile/", user_profile_url.profile, name='profile'),
    path('register/', reg.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='user/logout.html'), name='logout')
]
