# vendor/views.py
from rest_framework import generics, permissions
from .models import Vendor
from .serializers import VendorSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class VendorRegistrationView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.AllowAny]

class UserCreate(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLogin(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]



# for data2

from rest_framework import generics
from .models import Data2Registration
from .serializers import Data2RegistrationSerializer

class Data2RegistrationListCreate(generics.ListCreateAPIView):
    queryset = Data2Registration.objects.all()
    serializer_class = Data2RegistrationSerializer
