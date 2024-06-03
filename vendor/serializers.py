# vendor/serializers.py
from rest_framework import serializers
from .models import Vendor
from django.contrib.auth.models import User

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# for data2
from rest_framework import serializers
from .models import Data2Registration

class Data2RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data2Registration
        fields = '__all__'