from django.urls import path
from  .  import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('projects/', views.project_list_create, name='project-list-create'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),
    path('tasks/', views.task_list_create, name='task-list- create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
]