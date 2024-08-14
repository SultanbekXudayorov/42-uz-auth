from rest_framework import serializers
from AuthApp.models import UserPhoneNumber
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=6)

class LoggedInUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoneNumber
        fields = ['id', 'phone_number']