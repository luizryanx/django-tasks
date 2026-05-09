from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import UpdateView
from .models import Tasks
from .forms import TasksForm
from django.urls import reverse_lazy

# def tasks_list(request):
#     tasks = Tasks.objects.all()
#     return render(request, "tasks/tasks_list.html", {"tasks": tasks})

class TasksListView(ListView):
    model = Tasks
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"

class TasksUpdateView(UpdateView):
    model = Tasks
    form_class = TasksForm
    template_name = "tasks/tasks_edit.html"
    success_url = reverse_lazy('tasks_list')
    def form_valid(self, form):    
        return super().form_valid(form)
    
class TasksDeleteView(DeleteView):
    model = Tasks
    template_name = "tasks/tasks_delete.html"
    success_url = reverse_lazy('tasks_list')