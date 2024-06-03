# ERP/urls.py
from django.contrib import admin as django_admin
from django.urls import path
from vendor.views import UserCreate, UserLogin, VendorRegistrationView
from .views import Data2RegistrationListCreate

urlpatterns = [
    # path('admin/', django_admin.site.urls),
    path('api/auth/register/', UserCreate.as_view(), name='register'),
    path('api/auth/login/', UserLogin.as_view(), name='login'),
    path('api/vendors/register/', VendorRegistrationView.as_view(), name='vendor-register'),
    path('Data2register/', Data2RegistrationListCreate.as_view(), name='Data2register'),
]


# # for data2

# from django.urls import path
# from .views import RegistrationListCreate

# urlpatterns = [
#     path('register/', RegistrationListCreate.as_view(), name='register'),
# ]
