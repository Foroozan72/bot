# auth/views.py

from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer , RegisterSerializer


class RegisterUserView(APIView):
    """
    User registration endpoint.
    """

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomLoginView(APIView):
    """
    Custom login view that accepts phone or email and password.
    """

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)