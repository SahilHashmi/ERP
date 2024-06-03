# urls.py

from django.urls import path
from .views import StateListCreate, StateRetrieveUpdateDestroy


from django.urls import path
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy

urlpatterns = [
    path('states/', StateListCreate.as_view(), name='state-list-create'),
    path('states/<int:pk>/', StateRetrieveUpdateDestroy.as_view(), name='state-detail'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
]



