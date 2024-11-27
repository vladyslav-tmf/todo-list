from django.shortcuts import render
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "todo/index.html", {"tasks": tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = "/"
