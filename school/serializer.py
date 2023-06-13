from rest_framework import serializers
from .models import Course,Student,Teacher

#Configuración de Serializers de entidades u .  u

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'