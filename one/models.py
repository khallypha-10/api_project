from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    student_id = models.IntegerField()
    department = models.CharField( max_length=150)
    enrolled_in = models.DateField(auto_now_add=True)

    
