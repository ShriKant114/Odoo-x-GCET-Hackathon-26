from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # You need this import!
from .views import register, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Authentication URLs (Login, Logout, Password management)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 2. Registration
    path('accounts/register/', register, name='register'),
    
    # 3. Dashboard (Home)
    path('dashboard/', dashboard, name='dashboard'),
    path('', dashboard, name='index'), # Root URL also points to dashboard
]