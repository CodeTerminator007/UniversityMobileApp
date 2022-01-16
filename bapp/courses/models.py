from xmlrpc.client import MININT
from django.db import models


class Course(models.Model):

    title = models.CharField( max_length=100,null=False)
    discription = models.CharField(max_length=150,null=True)
    credit_hours = models.IntegerField(max_length=5)



    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of Course."""
        return self.title
