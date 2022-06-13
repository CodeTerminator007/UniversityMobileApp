
from email.mime import base
from posixpath import basename

from announcements.views import AnnouncementView
from courses.views import (ClassViewset, CourseViewset, SubjectsViewset,
                           SubjectsViewsetfilterclass)
from django.urls import include, path
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter

from user import views

from .views import (AssignmentSubmissionViewSet, AssignmentViewSet,
                    AttendanceReportViewSet, AttendanceViewSet,
                    BulkattandanceView, LoginView, NormalStudentViewSet,
                    TimeTableViewSet,StudentpostViewSet ,SecondAssignmentViewSet,SecondAssignmentSubmissionViewSet,SimpleStudentViewSet ,QuizViewSet,QuestionViewSet,incorrect_answerViewSet ,QuizResultViewSet)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user/admin', views.AdminViewSet)
router.register(r'user/student', views.StudentViewSet)
router.register(r'user/faculty', views.FacultyViewSet)
router.register(r'announcement',AnnouncementView)
router.register(r'course',CourseViewset)
router.register(r'Subject',SubjectsViewset)
router.register(r'Subjectfilterclass',SubjectsViewsetfilterclass),
router.register(r'Class',ClassViewset)
router.register(r'Attendance',AttendanceViewSet)
router.register(r'AttendanceReport',AttendanceReportViewSet)
router.register(r'Timetable',TimeTableViewSet)
router.register(r'BulkAttendance', BulkattandanceView)
router.register(r'NormalStudentViewset', NormalStudentViewSet)
router.register(r'AssignmentViewSet', AssignmentViewSet)
router.register(r'AssignmentSubmissionViewSet', AssignmentSubmissionViewSet)
router.register(r'StudentPostViewset', StudentpostViewSet)
router.register(r'SecondAssignmentViewSet',SecondAssignmentViewSet)
router.register(r'SecondAssignmentSubmissionViewSet',SecondAssignmentSubmissionViewSet)
router.register(r'SimpleStudentViewSet',SimpleStudentViewSet)
router.register(r'Quiz',QuizViewSet)
router.register(r'Question',QuestionViewSet)
router.register(r'Incorrect_answers',incorrect_answerViewSet)
router.register(r'quizresult',QuizResultViewSet)



urlpatterns = [
    path('auth/login', LoginView.as_view()),
    path('', include(router.urls)),    
]
