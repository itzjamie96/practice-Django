from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.decorators.http import require_http_methods, require_POST
from django.http import HttpResponse
import random

# Create your views here.
def index(request):

    polls = Poll.objects.order_by('pk')
    context = {
        'polls':polls
    }

    return render(request, 'polls/index.html', context)


def detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    comments = poll.comment_set.all()
    context = {
        'poll':poll,
        'comments':comments
    }
    return render(request, 'polls/detail.html', context)


def createPoll(request):

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid:
            poll = form.save()
            return redirect('polls:detail', poll.pk)
            
    else:
        form = PollForm()
    context = {
        'form':form,
    }
    return render(request, 'polls/createPoll.html', context)


def updatePoll(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect('polls:detail', poll.pk)
    else:
        form = PollForm(instance=poll)
    
    context = {
        'form':form,
        'poll': poll,
    }
    return render(request, 'polls/updatePoll.html', context)


def deletePoll(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    poll.delete()
    return redirect('polls:index')


def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'POST':
        comment = Comment(poll=poll, content=request.POST['comment'])
        selected = request.POST['poll']

        if selected == 'choice1':
            poll.choice1_count += 1
        else:
            poll.choice2_count += 1
        
        poll.save()
        comment.save()

        return redirect('polls:detail', poll.pk)
    
    context = {
        'poll':poll,
    }
    return render(request, 'polls/detail.html', context)


def randomPoll(request):
    pks = Poll.objects.values_list('pk', flat=True)
    randomPk = random.choice(pks)
    return redirect('polls:detail', randomPk)
    