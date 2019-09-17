from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .models import *


def index(request):
    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        context = {
            'todos': todo_items
        }
        return render(request, 'todoapp/index.html', context)

    elif request.method == 'POST':
        title, status = request.POST['title'], True if len(request.POST.getlist('status')) > 0 else False
        description = request.POST['description']
        todo_item = TodoItem()
        todo_item.title = title
        todo_item.status = status
        todo_item.description = description
        todo_item.save()
        return HttpResponseRedirect(reverse('todoapp:index'))

    return HttpResponseBadRequest()


def details(request, pk):
    todo_item = get_object_or_404(TodoItem, pk=pk)

    if request.method == 'GET':
        context = {
            'todo': todo_item,
            'pk': pk
        }
        return render(request, 'todoapp/details.html', context)

    elif request.method == 'POST':
        title, status = request.POST['title'], True if len(request.POST.getlist('status')) > 0 else False
        description = request.POST['description']
        todo_item.title = title
        todo_item.status = status
        todo_item.description = description
        todo_item.save()
        return HttpResponseRedirect(reverse('todoapp:index'))

    return HttpResponseBadRequest()
