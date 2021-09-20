from django.db import models

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    mailing_address = models.CharField(max_length=200)
    gpa = models.CharField(max_length=200)



