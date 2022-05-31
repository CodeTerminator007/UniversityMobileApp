from rest_framework import serializers
from user.models import Courses ,Subjects,Class

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'

class SubjectsSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course_id.course_name')
    staff_name = serializers.ReadOnlyField(source='staff_id.username')

    class_name = serializers.ReadOnlyField(source='class_id.class_name')
    class_semaster = serializers.ReadOnlyField(source='class_id.semaster')
    class_sec = serializers.ReadOnlyField(source='class_id.sec')


    class Meta:
        model = Subjects
        fields = '__all__'        

class ClassSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course_id.course_name')

    class Meta:
        model = Class
        fields = '__all__'        