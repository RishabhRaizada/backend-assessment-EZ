from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import UploadedFile, User
from .serializers import UploadFileSerializer, UserSerializer, SignupSerializer
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token

import os

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if 'role' in request.data and request.data['role'] != 'client':
            return Response({"error": "Only 'client' users can register."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UploadFileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.FILES) 

        if request.user.role != 'ops':
            return Response({"error": "Only Ops users can upload files."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'client':
            return Response({"error": "Only Client users can list files."}, status=status.HTTP_403_FORBIDDEN)
        
        files = UploadedFile.objects.all()
        file_data = [{"file_id": f.id, "file_name": f.file.name} for f in files]
        
        return Response({"files": file_data}, status=status.HTTP_200_OK)

class DownloadFileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        if request.user.role != 'client':
            return Response({"error": "Only Client users can download files."}, status=status.HTTP_403_FORBIDDEN)
        
        encrypted_url = "https://yourdomain.com/download/secure/" + str(file_id)
        return Response({"download-link": encrypted_url, "message": "success"}, status=status.HTTP_200_OK)

