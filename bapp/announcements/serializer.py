from .models import Announcement
from rest_framework import serializers

class AnnouncementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Announcement
        fields = ['image','title','detail','Arthur','created_at']