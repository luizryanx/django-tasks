from django import forms 
from .models import Tasks

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status']

class TasksFormCreate(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status', 'due_date']