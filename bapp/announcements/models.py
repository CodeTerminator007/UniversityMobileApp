from pyexpat import model
from turtle import title
from django.db import models
from user.models import User
from django.db.models.deletion import DO_NOTHING

class Announcement(models.Model):
    """Model definition for Announcement."""

    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000,blank=True)
    # image = models.ImageField(upload_to='uploads',null=True)
    Arthur = models.ForeignKey(User,on_delete=DO_NOTHING,related_name='Arthur')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Announcement."""

        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        """Unicode representation of Announcement."""
        return self.title
