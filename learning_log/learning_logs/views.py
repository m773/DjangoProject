from urllib import request
from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """show all topics"""
    topiclist=Topic.objects.order_by('date_added')
    context={'topics':topiclist}
    return render(request,'learning_logs/topics.html',context)


def topic(request, topic_id):
    """Show a single topic and its entries."""
    mytopic = Topic.objects.get(id=topic_id)
    myentries = mytopic.entry_set.order_by('-date_added')
    context = {'topic': mytopic, 'entries': myentries}
    return render(request, 'learning_logs/topic.html', context)
