from django.shortcuts import render, redirect

# import models
from .models import *

# import forms
from .forms import *


# 메인 화면
def list(request):

    # bring tasks from models
    tasks = Task.objects.all()

    # bring form
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('tasks:list')

    # throw the tasks in the context
    context = {
        'tasks':tasks,
        'form':form
    }

    # pass the context to the views!
    return render(request,'tasks/list.html', context)


def update(request, pk):

    task = Task.objects.get(pk=pk)

    # prefill the form with task with pk for us
    form = TaskForm(instance=task)

    # throwing new data but it's an updated version of the original task
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks:list')

    context = {
        'form': form
    }

    return render(request,'tasks/update.html', context)


def delete(request, pk):

    item = Task.objects.get(pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('tasks:list')

    context = {
        'item':item
    }

    return render(request, 'tasks/delete.html', context)