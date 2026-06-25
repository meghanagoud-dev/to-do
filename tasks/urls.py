from django.urls import path
from . import views
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    return redirect('login')
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
        path('logout/', logout_view, name='logout'),
]