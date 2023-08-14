from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def create_topic (request):
    if request.method=="POST":
        tn=request.POST["topic"]
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse(" data inserted succesfull")
    return render(request,'create_topic.html')