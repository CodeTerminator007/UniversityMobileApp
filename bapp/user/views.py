from django.shortcuts import render
from rest_framework import viewsets , status
import user
from django.conf import settings
import jwt
from django.contrib import auth
from rest_framework.response import Response
from .serializer import UserSerializer , StudentSerializer , FacultySerializer ,AdminSerializer ,LoginSerializer
from .models import User , Admin , Student ,Faculty
from user import serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import GenericAPIView

# Create your views here.


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:

            auth_token = jwt.encode({'username': user.username}, "secret", algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    
# class CreateUserviewset(viewsets.ViewSet):
#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         if request.data['is_student'] == True:
#             studentser = StudentSerializer(user=user)
#             if studentser.is_valid():
#                 studentser.save()
#                 return Response({'msg':'Student Created'},status=status.HTTP_201_CREATED)
#             return Response(studentser.errors,status=status.HTTP_400_BAD_Request)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'User Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_Request)





class AdminViewSet(viewsets.ModelViewSet):

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class FacultyViewSet(viewsets.ModelViewSet):

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]