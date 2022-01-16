from django.contrib import admin
from .models import User,Admin,Student,Faculty
from announcements.models import Announcement
# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Announcement)
