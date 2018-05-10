from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    tutor = models.CharField(max_length=50)
    number_lessons = models.IntegerField()
    workload = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
