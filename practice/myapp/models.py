from django.db import models

# Create your models here.
class Student(models.Model):
    COURSE=[
        ('BT', 'Bachelor of Technology'),
        ('BBA', 'Bachelor of Business Administration'),
        ('BCom', 'Bachelor of Commerce'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=4, choices=COURSE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"