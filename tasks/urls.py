from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.models import User

# Auto create superuser - login ayyaka ee 3 lines delete cheyyali
if not User.objects.filter(username='meghana').exists():
    User.objects.create_superuser('meghana', 'meghana@gmail.com', 'meghana123')


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create-admin/', views.create_admin), 
]
