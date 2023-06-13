from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('Teacher', views.TeacherView, 'Teacher')
router.register('Course', views.CourseView, 'Course')
router.register('Student', views.StudentView, 'Student')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/StudentCourse/<int:student_id>', views.student_course),
    path('api/TeacherCourse/<int:teacher_id>', views.teacher_course),
    path('docs/', include_docs_urls(title="School_API"))
]
