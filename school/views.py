from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TeacherSerialiazer, StudentSerializer, CourseSerializer
from .models import Teacher,Course, Student
# Create your views here.

class TeacherView(viewsets.ModelViewSet):
    serializer_class = TeacherSerialiazer
    queryset = Teacher.objects.all()

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

@api_view(["GET"])
def student_course(request, student_id):
    try:
        student = Student.objects.get(id= student_id)
    except Student.DoesNotExist:
        return Response ({'message': 'Estudiante no encontrado... u_u'}, status=404)

    courses = student.course_set.all()
    course_list = [course.name for course in courses]

    data = {
        'nombre': student.name+' '+student.lastName,
        'materias': course_list
    }
    return Response(data)

@api_view(["GET"])
def teacher_course(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id= teacher_id)
    except Teacher.DoesNotExist:
        return Response ({'message': 'Maestro no encontrado... u_u'}, status=404)

    courses = teacher.course_set.all()
    course_list = [course.name for course in courses]

    data = {
        'nombre':   teacher.name +' '+teacher.lastName,
        'materias': course_list
    }
    return Response(data)
