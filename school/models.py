from django.db import models

# Create your models here.

#Entidad Estudiante u  . u
class Student(models.Model):
    name = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.name + ' ' + self.lastName

#Entidad Maestro o . 0
class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.name + ' ' + self.lastName

#Entidad Materia U - u
class Course(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    Student = models.ManyToManyField(Student)
    Teacher = models.ForeignKey(Teacher, models.CASCADE, default=1)
    def __str__(self):
        return self.name





