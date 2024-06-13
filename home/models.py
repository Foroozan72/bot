from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 200 , null = False , blank = False)
    desc = models.TextField(default="this is student")

class Lessons(models.Model):
    name = models.CharField(max_length = 200 , null = False , blank = False)
    desc = models.TextField(default="this is lesson")

    def __str__(self):
        return self.name
    
class package(models.Model):
    name = models.CharField(max_length = 200 , null = False , blank = False)
    desc = models.TextField(default="this is package")

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 200 , null = False , blank = False)
    desc = models.TextField(default="this is course")
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


# Create your models here.
