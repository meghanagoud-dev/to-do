from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title:
            Task.objects.create(user=request.user, title=title, due_date=due_date if due_date else None)
        return redirect('home')
    
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    return render(request, 'home.html', {'tasks': tasks})

