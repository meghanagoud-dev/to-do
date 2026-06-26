from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task

@login_required  # IDHI LINE 7 KI ADD CHEY
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title:  # 'request.user.is_authenticated' teesesam endukante @login_required undi
            Task.objects.create(
                user=request.user, 
                title=title, 
                due_date=due_date if due_date else None  # EMPTY AYITHE NONE PETTU
            )
        return redirect('home')
    
    # Ee 3 lines teesesey - @login_required valla avasaram ledu
    tasks = Task.objects.filter(user=request.user).order_by('-id')
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
def create_admin(request):
    from django.contrib.auth.models import User
    User.objects.filter(username='mawa').delete()
    User.objects.create_superuser('mawa', 'mawa@gmail.com', 'Mawa@1234')
    return HttpResponse("DONE Mawa! Username: mawa | Password: Mawa@1234")