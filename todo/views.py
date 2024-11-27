from django.shortcuts import render

from todo.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "todo/index.html", {"tasks": tasks})
