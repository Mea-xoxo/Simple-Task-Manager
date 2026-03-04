from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user)
    return render(request,'tasks-temps/task_list.html',{'tasks':tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority =request.POST.get('priority')
        Task.objects.create(title = title, description = description, due_date=due_date ,user = request.user)
        return redirect('task_list')
    return render(request,'tasks-temps/task_form.html')

@login_required
def task_complete(request,pk):
    task= get_object_or_404(Task,pk = pk)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def task_edit(request,pk):
    task = get_object_or_404(Task, pk = pk,user = request.user)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')       
        task.save()
        return redirect('task_list')
    return render(request,'tasks-temps/task_edit.html',{'task': task})
        
        
@login_required
def task_delete(request,pk):
    task = get_object_or_404 (Task, pk = pk)
    task.delete()
    return redirect('task_list')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username = username, password = password)
        return redirect('login')
    return render(request,'tasks-temps/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user:
            login(request,user)
            return redirect('task_list')
        return render(request,'tasks-temps/login.html', {'error': 'Invalid Username or password'})
    return render(request,'tasks-temps/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


# Create your views here.
