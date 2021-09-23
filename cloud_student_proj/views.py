from django.shortcuts import render
from . import forms
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import render,redirect
from cloud_student_proj.models import Student
from .forms import ContentForm
from django.contrib import messages

class AddView(TemplateView):
    template_name = 'add.html'

class HomeView(TemplateView):
    template_name = 'home.html'

def show(request):
    students = Student.objects.all()
    return render(request,"profile.html",{'student':students})

def search_show(request):
    students = Student.objects.all()
    return render(request,"profile.html",{'student':students})

def post(request ):                                                                                             
    post_list = Post.objects.order_by('id')
    form = ContentForm()
    return render(request, 'posts/success.html',
        {'post': post_list,
        'form':form},
    )                                                                                                           
def content_get(request):
    if request.method == 'POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

def get_question(request):
    form = forms.ContentForm()

    if request.method == 'POST':
        form = forms.ContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ContentForm()

    return render(request, 'success.html', {'form':form})

class SearchResultsView(ListView):
     model = Student
     template_name = 'search_results.html'

     def get_queryset(self): # new
         query = self.request.GET.get('q')
         object_list = Student.objects.filter(
             Q(student_id__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query) 
         )
         return object_list

def my_form(request):
  if request.method == "POST":
    form = ContentForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Student Added!')
  else:
      form = ContentForm()
  return render(request, 'add.html', {'form': form})

