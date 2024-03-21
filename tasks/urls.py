"""Определяет схемы URL для Task."""

from django.urls import path, include
from . import views

app_name = 'tasks'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('new_task/', views.new_task, name='new_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')
]