from rest_framework import serializers
from user.models import Courses ,Subjects,Class

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'

class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = '__all__'        

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'        