from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

def index(request):
    """Домашняя страница приложения Task"""
    return render(request, 'tasks/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user)
    sorted_tasks = sorted(tasks, key=lambda x: (x.completed, x.end_date, x.priority))
    context = {'tasks': sorted_tasks}
    return render(request, 'tasks/tasks.html', context)

@login_required
def task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'tasks/task.html', context)

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    tasks = Task.objects.filter(owner=request.user)
    sorted_tasks = sorted(tasks, key=lambda x: (x.completed, x.end_date, x.priority))
    context = {'tasks': sorted_tasks}
    return render(request, 'tasks/tasks.html', context)

@login_required
def edit_task(request, task_id):
    """Редактирует существующую задачу."""
    task = Task.objects.get(id=task_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей задачи.
        form = TaskForm(instance=task)
    else:
        # Отправка данных POST; обработать данные.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task', task_id=task_id)
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)

@login_required
def new_task(request):
    """Создает новую задачу."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TaskForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('tasks:tasks')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)