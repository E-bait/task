from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date', 'completed', 'priority']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'start_date': 'Start date',
            'end_date': 'End date',
            'completed': 'Completed',
            'priority': 'Priority',
        }