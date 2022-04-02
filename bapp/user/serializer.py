from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import Permission
from rest_framework import serializers
from .models import Attendance, AttendanceReport, User , Student , Faculty , Admin

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ['id','username','email','password','first_name','last_name','is_admin','is_student','is_faculty']
        


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin 
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student 
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty 
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255,min_length=2)
    password = serializers.CharField(max_length=65,min_length=8,write_only=True)
    class Meta:
        model = User
        fields = ['username','password']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance 
        fields = '__all__'

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = '__all__'