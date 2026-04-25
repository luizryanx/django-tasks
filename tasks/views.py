from django.shortcuts import render
from django.views.generic import ListView
from .models import Tasks

# def tasks_list(request):
#     tasks = Tasks.objects.all()
#     return render(request, "tasks/tasks_list.html", {"tasks": tasks})

class TasksListView(ListView):
    model = Tasks
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"