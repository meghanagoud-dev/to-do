from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title and request.user.is_authenticated:
            Task.objects.create(user=request.user, title=title, due_date=due_date if due_date else None)
        return redirect('home')
    
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')
    else:
        tasks = []
        
    return render(request, 'home.html', {'tasks': tasks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('home')

@login_required  
def complete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')