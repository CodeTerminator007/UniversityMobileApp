from announcements.models import Announcement
from django.contrib import admin

from .models import (Admin, Assignment, AssignmentResult, AssignmentSubmission,
                     Attendance, AttendanceReport, Class, Courses, Faculty,
                     Question, Quiz, QuizResult, Result, Student,
                     SubjectResult, Subjects, Timetable, User,
                     incorrect_answers)

# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Announcement)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Class)
admin.site.register(Attendance)
# admin.site.register(AttendanceReport)
admin.site.register(Timetable)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(incorrect_answers)
admin.site.register(QuizResult)
admin.site.register(AssignmentResult)
admin.site.register(Result)
admin.site.register(SubjectResult)

@admin.register(AttendanceReport)
class AttendanceReportAdmin(admin.ModelAdmin):
    '''Admin View for AttendanceReport'''

    list_display = ('susername', 'status', 'subject_id')
    list_filter = ('subject_id', 'student_id')

    def susername(self,obj):
        return obj.student_id.user.username
