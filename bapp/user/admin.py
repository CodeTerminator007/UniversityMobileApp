from django.contrib import admin
from .models import User,Admin,Student,Faculty
from announcements.models import Announcement
from courses.models import Course , Class

# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Announcement)
admin.site.register(Course)
admin.site.register(Class)


