# from django.db import models
# from user.models import User
# import datetime
# class Assignment(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     marks = models.CharField(max_length=20)
#     duration = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)    

#     class Meta:
#         """Meta definition for Assignment."""

#         verbose_name = 'Assignment'
#         verbose_name_plural = 'Assignments'

#     def __str__(self):
#         """Unicode representation of Assignment."""
#         pass


# class AssignmentSubmission(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     university_id = models.CharField(max_length=100)
#     content = models.TextField(null=True, blank=True)
#     file = models.FileField(null=True, blank=True)

#     class Meta:
#         """Meta definition for AssignmentSubmission."""

#         verbose_name = 'AssignmentSubmission'
#         verbose_name_plural = 'AssignmentSubmissions'

#     def __str__(self):
#         """Unicode representation of AssignmentSubmission."""
#         pass
