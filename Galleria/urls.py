from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', user_views.register, name="register"),
    path('profile/', include("user_profile.urls")),
    path('items/', include('items.urls')),
    path('profile/', include("user_profile.urls")),
    path('business/', include("business_account.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

