from rest_framework import serializers
from .models import UploadedFile, User

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['file']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data['role']
        )
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password', 'role'] 

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            role=validated_data['role'], 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user