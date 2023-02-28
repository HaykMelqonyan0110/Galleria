from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from user import views as reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path('login/', views.LoginView(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView(template_name='user/logout.html'), name='logout'),
    path('register/', reg.register, name="register"),
]
