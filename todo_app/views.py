from django.shortcuts import render
from todo_app.models import Task

# Create your views here.

def home(response):
  
    if response.method=='POST':
        name=response.POST['name']
        desc=response.POST['desc']
        temp=Task(name=name, desc=desc)
        temp.save()
        query = {'context':True}
    else:
        query =  {'context':False}
    return render (response,'home.html',query)

def task(response):
    tasks_all = Task.objects.all()
    dic = {'tasks':tasks_all}
    return render (response,'task.html',dic)


