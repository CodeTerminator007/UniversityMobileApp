from django.db.models.deletion import CASCADE
from xmlrpc.client import MININT
from django.db import models

# class Course(models.Model):

#     title = models.CharField( max_length=100,null=False)
#     discription = models.CharField(max_length=150,null=True)
#     credit_hours = models.IntegerField()



#     class Meta:
#         """Meta definition for Course."""

#         verbose_name = 'Course'
#         verbose_name_plural = 'Courses'

#     def __str__(self):
#         """Unicode representation of Course."""
#         return self.title

# class Class(models.Model):

#     class_name = models.CharField(max_length=50)
#     sec = models.CharField(max_length=1)
#     courses = models.ManyToManyField(Course, related_name='classes')


#     class Meta:
#         """Meta definition for Class."""

#         verbose_name = 'Class'
#         verbose_name_plural = 'Classs'

#     def __str__(self):
#         """Unicode representation of Class."""
#         return self.class_name
