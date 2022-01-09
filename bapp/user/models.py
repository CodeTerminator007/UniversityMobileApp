from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.





class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='uploads')


class Admin(models.Model):
    """Model definition for Admin."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    

    class Meta:
        """Meta definition for Admin."""

        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        """Unicode representation of Admin."""
        pass


class Student(models.Model):
    """Model definition for Student."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        pass


class Faculty(models.Model):
    """Model definition for Faculty."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    
    class Meta:
        """Meta definition for Faculty."""

        verbose_name = 'Faculty'
        verbose_name_plural = 'Facultys'

    def __str__(self):
        """Unicode representation of Faculty."""
        pass
