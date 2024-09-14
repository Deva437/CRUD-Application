from django.shortcuts import render,redirect
from .forms import *
from .models import *


def Index(request):
    return render(request,'home.html')

def HomePage(request):
    return render(request,'home.html')


def AddTask(request):
    if request.method == 'POST':
        main_form = Main_Form(request.POST,request.FILES)
        
        if main_form.is_valid():
            main_form.save()
    

    context = { 
        'add_form': Main_Form()
               }       
    return render (request, 'add_task.html', context)



def ViewTask(request):
    context ={
        "view_task" : Mainclass.objects.all()
     }
     
    return render(request, 'view_task.html', context)


def Delete_Task(request, id):
    selected_data = Mainclass.objects.get(id=id)
    selected_data.delete() 
    return redirect('/viewtask/')



def Task_update(request, id):
    selected_task = Mainclass.objects.get(id=id)
    
    if request.method == "POST":
        task = Main_Form(request.POST,request.FILES,instance=selected_task)
        if task.is_valid():
            task.save()
            return redirect('/viewtask/')
    context = {
        'task_update': Main_Form(instance=selected_task)
    }
    return render(request, 'update.html', context)
    

def Filter_Priority(request):
    filter_priority=request.GET.get('priority')
    task=Mainclass.objects.filter(task_priority=filter_priority) 
    if task==filter_priority:
        print(1)
        return filter_priority
    else:
        print(2) 
        Mainclass.objects.all()
    context={
        'view_task':task
    }
    return render(request, 'view_task.html', context )
