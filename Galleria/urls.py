from django.contrib import admin
from user_profile import views as profile_views
from django.urls import path, include
from django.contrib.auth import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', user_views.register, name="register"),
    path('profile/', profile_views.profile, name='profile')
]


