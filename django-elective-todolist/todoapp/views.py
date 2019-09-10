from django.shortcuts import render
from .models import *


def index(request):
    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        context = {
            'todos': todo_items
        }
        return render(request, 'todoapp/index.html', context)