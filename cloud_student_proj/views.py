from django.shortcuts import render

from django.shortcuts import render,redirect
from cloud_student_proj.models import Student

def show(request):
    students = Student.objects.all()
    return render(request,"profile.html",{'student':students})