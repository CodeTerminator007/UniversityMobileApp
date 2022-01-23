from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from courses.models import Class
from django.db.models.signals import post_save
# Create your models here.





class User(AbstractUser):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='uploads',null=True)

class Admin(models.Model):
    """Model definition for Admin."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    portal = models.CharField(null=True,max_length=200)

    class Meta:
        """Meta definition for Admin."""

        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        """Unicode representation of Student."""
        return self.user.username

    def create_admin(sender,instance,created,**kwargs):
        if created:
            if instance.is_admin == True:
                Admin.objects.create(user=instance)
                print("Admin Created")
    post_save.connect(create_admin,sender=User)

    


class Student(models.Model):
    """Model definition for Student."""

    the_class = models.ForeignKey(Class,on_delete=CASCADE,related_name='studentsforclass',null=True,blank=True)

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True,related_name='student')

    #gender
    roll_num = models.IntegerField(default=100) 

    address = models.TextField(null=True)
    # course_id =
     
    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return self.user.username

    def save(self, *args, **kwargs):
        self.roll_num = self.roll_num + 1
        super().save(*args, **kwargs)  # Call the "real" save() method.
        
    def create_student(sender,instance,created,**kwargs):
        if created:
            if instance.is_student == True:
                Student.objects.create(user=instance)
                print("Student Created")
    post_save.connect(create_student,sender=User)


class Faculty(models.Model):
    """Model definition for Faculty."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    
    class Meta:
        """Meta definition for Faculty."""

        verbose_name = 'Faculty'
        verbose_name_plural = 'Facultys'

    def __str__(self):
        """Unicode representation of Faculty."""
        return self.user.username

    def create_faculty(sender,instance,created,**kwargs):
        if created:
            if instance.is_faculty == True:
                Faculty.objects.create(user=instance)
                print("Faculty Created")
    post_save.connect(create_faculty,sender=User)
