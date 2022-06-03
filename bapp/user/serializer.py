from dataclasses import fields
from unittest.util import _MAX_LENGTH

from django.contrib.auth.models import Permission
from pyexpat import model
from rest_framework import serializers
from rest_framework_bulk import (BulkListSerializer, BulkSerializerMixin,
                                 ListBulkCreateUpdateDestroyAPIView)

from .models import (Admin, Assignment, AssignmentSubmission, Attendance,
                     AttendanceReport, Faculty, Student, Timetable, User)


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    class Meta:
        model = User 
        fields = ['id','username','email','password','first_name','last_name','is_admin','is_student','is_faculty','phone_number1','phone_number2','gender','last_education_degree','Dob','cnic','profile_image']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
class StudentPostSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    course = serializers.CharField(source='course_id.course_name')
    the_class = serializers.CharField(source='the_class.class_name')
    address = serializers.CharField(max_length=600,allow_blank=True)
    class Meta:
        model = User 
        fields = ['id','username','email','password','first_name','last_name','is_admin','is_student','is_faculty','phone_number1','phone_number2','gender','last_education_degree','Dob','cnic','profile_image','course','the_class','address']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        

class AdminSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')



    class Meta:
        model = Admin 
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')


    class Meta:
        model = Student 
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    
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
class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'


class BulkAttandanceSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        list_serializer_class = BulkListSerializer
        fields = '__all__'

class StudentAttendanceReportSeralizer(serializers.Serializer):
    CourseName = serializers.CharField()
    TeacherName = serializers.CharField()
    Lectures = serializers.IntegerField()
    Present = serializers.IntegerField()
    Absents = serializers.IntegerField()
    Percent = serializers.IntegerField()


class AssignmentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(required=False)
    class Meta:
        model =  Assignment
        fields =  ['id','faculty','Title','detail','submission_datetime','document','subject','status','marks','class_id']

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    document = serializers.FileField(required=False)
    class Meta:
        model =  AssignmentSubmission
        fields =  ['id','assignment','student','document','comment','marks','submission_datetime']

