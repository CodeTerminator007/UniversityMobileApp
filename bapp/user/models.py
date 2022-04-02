from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
# Create your models here.





class User(AbstractUser):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='uploads',null=True)


class Courses(models.Model):
    """Model definition for Courses."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        """Meta definition for Courses."""

        verbose_name = 'Courses'
        verbose_name_plural = 'Coursess'

    def __str__(self):
        """Unicode representation of Courses."""
        pass

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

    
class Class(models.Model):

    class_name = models.CharField(max_length=50)
    sec = models.CharField(max_length=1)

    class Meta:
        """Meta definition for Class."""

        verbose_name = 'Class'
        verbose_name_plural = 'Classs'

    def __str__(self):
        """Unicode representation of Class."""
        return self.class_name


class Student(models.Model):
    """Model definition for Student."""
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
    the_class = models.ForeignKey(Class,on_delete=CASCADE,related_name='studentsforclass',null=True,blank=True)
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True,related_name='student')
    roll_num = models.IntegerField(default=100) 
    address = models.TextField(null=True)
     
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





class Subjects(models.Model):
    """Model definition for Subjects."""

    # TODO: Define fields here
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1) #need to give defauult course
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        """Meta definition for Subjects."""

        verbose_name = 'Subjects'
        verbose_name_plural = 'Subjectss'

    def __str__(self):
        """Unicode representation of Subjects."""
        pass

class Attendance(models.Model):
    """Model definition for Attendance."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Attendance."""

        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        """Unicode representation of Attendance."""
        pass


class AttendanceReport(models.Model):
    """Model definition for AttendanceReport."""
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        """Meta definition for AttendanceReport."""

        verbose_name = 'AttendanceReport'
        verbose_name_plural = 'AttendanceReports'

    def __str__(self):
        """Unicode representation of AttendanceReport."""
        pass


# class LeaveReportStudent(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     leave_date = models.CharField(max_length=255)
#     leave_message = models.TextField()
#     leave_status = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()


# class LeaveReportStaff(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     leave_date = models.CharField(max_length=255)
#     leave_message = models.TextField()
#     leave_status = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()


# class FeedBackStudent(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()


# class FeedBackStaffs(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()    
