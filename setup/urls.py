"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import TasksListView, TasksUpdateView, TasksDeleteView,TasksCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', tasks_list, name = 'tasks_list'),
    path('', TasksListView.as_view(), name = 'tasks_list'),
    path('tasks/<int:pk>/edit/', TasksUpdateView.as_view(), name = 'tasks_edit'),
    path('tasks/<int:pk>/delete/', TasksDeleteView.as_view(), name = 'tasks_delete'),
    path('tasks/create/', TasksCreateView.as_view(), name = 'tasks_create'),
]
