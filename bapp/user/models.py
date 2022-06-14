from datetime import datetime
from email.policy import default
from statistics import mode
from xml.parsers.expat import model

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save


class User(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),)


    Education_Degree = (
        ('Matric/O level','Matric/O level'),
        ('Intermediate/DAE/A level','Intermediate/DAE/A level'),
        ('B.Sc English literature','B.Sc English literature'),
        ('B.Sc Accounting and Finance','B.Sc Accounting and Finance'),
        ('B.Sc Physics','B.Sc Physics'),
        ('B.Sc Electronics','B.Sc Electronics'),
        ('B.Sc Mathematics','B.Sc Mathematics'),
        ('B.Sc Electrical   ','B.Sc Electrical'),
        ('B.Sc Urdu','B.Sc Urdu'),
        ('B.Sc Compueter Science','B.Sc Compueter Science'),
        ('B.Sc Commerce','Commerce'),
        ('B.Sc Mechanical Engineering','B.Sc Mechanical Engineering'), 
        ('MS Computer Science','MS Computer Science'), 
        ('MS Electronics','MS Electronics'), 
        ('MS English literature','MS English literature'), 
        ('MS Accounting and Finance','MS Accounting and Finance'), 
        ('MS Physics','MS Physics'), 
        ('MS Electrical','MS Electrical'), 
        ('MS Mathematics','MS Mathematics'), 
        ('MS Urdu','MS Urdu'),
    )
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_number1 = models.CharField(validators=[phone_regex], max_length=13, blank=True) 
    phone_number2 = models.CharField(validators=[phone_regex], max_length=13, blank=True,null=True) 
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default=1)
    last_education_degree = models.CharField(max_length=27, choices=Education_Degree,default=1,null=True,blank=True)
    Dob = models.DateField(null=True)
    cnic_regex = RegexValidator(regex=r'^[0-9]{5}-[0-9]{7}-[0-9]{1}$', message="Cnic must be entered in the format: '11111-1111111-1'. Cnic must be entered with dashes.")
    cnic = models.CharField(validators=[cnic_regex], max_length=15, blank=False) 

class Courses(models.Model):
    """Model definition for Courses."""

    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        """Meta definition for Courses."""

        verbose_name = 'Courses'
        verbose_name_plural = 'Coursess'

    def __str__(self):
        """Unicode representation of Courses."""
        return self.course_name


    
class Class(models.Model):

    class_name = models.CharField(max_length=50)
    sec = models.CharField(max_length=1)
    semaster = models.CharField(max_length=50)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Class."""

        verbose_name = 'Class'
        verbose_name_plural = 'Classs'

    def __str__(self):
        """Unicode representation of Class."""
        return (f"{self.course_id.course_name} {self.class_name} {self.semaster} section {self.sec}")


class Faculty(models.Model):
    """Model definition for Faculty."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    # address = 
    
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
    post_save.connect(create_faculty,sender=User)

class Subjects(models.Model):
    """Model definition for Subjects."""

    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1) #need to give defauult course
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        """Meta definition for Subjects."""

        verbose_name = 'Subjects'
        verbose_name_plural = 'Subjectss'

    def __str__(self):
        """Unicode representation of Subjects."""
        return self.subject_name


class Student(models.Model):
    """Model definition for Student."""
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
    the_class = models.ForeignKey(Class,on_delete=CASCADE,related_name='studentsforclass',null=True,blank=True,default=1)
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
        self.roll_num = self.user.id + 1
        super().save(*args, **kwargs)  
        
    def create_student(sender,instance,created,**kwargs):
        if created:
            if instance.is_student == True:
                Student.objects.create(user=instance)
    post_save.connect(create_student,sender=User)


class Admin(models.Model):
    """Model definition for Admin."""

    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)

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
    




class Attendance(models.Model):
    """Model definition for Attendance."""

    subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Attendance."""

        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    # def __str__(self):
    #     """Unicode representation of Attendance."""
    #     pass


class AttendanceReport(models.Model):
    """Model definition for AttendanceReport."""

    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        """Meta definition for AttendanceReport."""

        verbose_name = 'AttendanceReport'
        verbose_name_plural = 'AttendanceReports'

    # def __str__(self):
    #     """Unicode representation of AttendanceReport."""
    #     pass

class Timetable(models.Model):
    """Model definition for Timetable."""
    DAYS_OF_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),)



    sub = models.CharField(max_length = 100, blank = True)
    subhoursstart = models.TimeField(auto_now=False, auto_now_add=False)
    subhoursend = models.TimeField(auto_now=False, auto_now_add=False)
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    room  = models.IntegerField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        """Meta definition for Timetable."""

        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'

    def __str__(self):
        """Unicode representation of Timetable."""
        pass


class Assignment(models.Model):
    """Model definition for Assignment."""
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    Title = models.CharField( max_length=50)
    detail = models.TextField()
    submission_date = models.DateField(auto_now=False,auto_now_add=False)
    submission_time = models.TimeField(auto_now=False,auto_now_add=False)
    document = models.FileField(max_length=100,upload_to="Assignment")
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    marks = models.IntegerField()
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE)
    

    class Meta:
        """Meta definition for Assignment."""

        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        """Unicode representation of Assignment."""
        return self.Title

class AssignmentSubmission(models.Model):
    """Model definition for AssignmentSubmission."""

    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    document = models.FileField(max_length=100,upload_to="Assignment")
    comment = models.TextField(null=True,blank=True)
    marks = models.IntegerField(default=0)
    submission_datetime = models.DateTimeField(auto_now_add=True)
    


    class Meta:
        """Meta definition for AssignmentSubmission."""

        verbose_name = 'AssignmentSubmission'
        verbose_name_plural = 'AssignmentSubmissions'

    def __str__(self):
        """Unicode representation of AssignmentSubmission."""
        return f"{self.assignment.Title} {self.assignment.class_id.course_id.course_name} {self.assignment.class_id.class_name} {self.assignment.class_id.sec}"



class Quiz(models.Model):
    """Model definition for Quiz."""
    title = models.CharField(max_length=50)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")
    quizDate = models.DateField()
    class Meta:
        """Meta definition for Quiz."""

        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizs'

    def __str__(self):
        """Unicode representation of Quiz."""
        return self.title

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    """Model definition for Question."""

    question = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='allquestions')
    correct_answer = models.CharField(max_length=300)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.question

class incorrect_answers(models.Model):
    """Model definition for incorrect_answers."""

    Question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='incorrect_answers')
    content = models.CharField(max_length=200)
    class Meta:
        """Meta definition for incorrect_answers."""

        verbose_name = 'incorrect_answers'
        verbose_name_plural = 'incorrect_answerss'

    def __str__(self):
        """Unicode representation of incorrect_answers."""
        return self.content



class QuizResult(models.Model):
    """Model definition for QuizResult."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='quizresult_quiz')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='quizresult_student')
    marks = models.IntegerField()
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    outofmarks = models.IntegerField(default=0)
    class Meta:
        """Meta definition for QuizResult."""

        verbose_name = 'QuizResult'
        verbose_name_plural = 'QuizResults'

    def __str__(self):
        """Unicode representation of QuizResult."""        
        return f"{self.student.user.username} {self.quiz.title}"


# class LeaveReportStudent(models.Model):
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     leave_date = models.CharField(max_length=255)
#     leave_message = models.TextField()
#     leave_status = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class LeaveReportStaff(models.Model):
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     leave_date = models.CharField(max_length=255)
#     leave_message = models.TextField()
#     leave_status = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class FeedBackStudent(models.Model):
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class FeedBackStaffs(models.Model):
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
