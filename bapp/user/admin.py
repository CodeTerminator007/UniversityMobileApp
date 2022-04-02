from django.contrib import admin
from .models import User,Admin,Student,Faculty
from announcements.models import Announcement
from .models import Courses ,Subjects , Class ,Attendance,AttendanceReport


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
admin.site.register(AttendanceReport)


