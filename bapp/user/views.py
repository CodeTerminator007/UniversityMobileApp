from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer , StudentSerializer , FacultySerializer ,AdminSerializer
from .models import User , Admin , Student ,Faculty

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer



class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class FacultyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
