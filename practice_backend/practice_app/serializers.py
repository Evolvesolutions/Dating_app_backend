from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import UserDetail

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    mail_id = serializers.EmailField()
    password = serializers.CharField()
