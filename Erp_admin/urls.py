# erp_project/urls.py
from django.contrib import admin as django_admin
from django.urls import path
from Erp_admin.views import UserCreate, UserLogin

urlpatterns = [
    # path('admin/', django_admin.site.urls),
    path('api/auth/register/', UserCreate.as_view(), name='register'),
    path('api/auth/login/', UserLogin.as_view(), name='login'),
]
