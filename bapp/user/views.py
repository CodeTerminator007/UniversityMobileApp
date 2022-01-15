from django.shortcuts import render
from rest_framework import viewsets , status
import user
from rest_framework.response import Response
from .serializer import UserSerializer , StudentSerializer , FacultySerializer ,AdminSerializer
from .models import User , Admin , Student ,Faculty
from user import serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

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