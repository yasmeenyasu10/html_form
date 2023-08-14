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

def webpage(request):
    d={'to':Topic.objects.all()}
    if request.method=='POST':
        tn=request.POST['topic']
        to=Topic.objects.get(topic_name=tn)
        n=request.POST['name']
        u=request.POST['url']
        Wo=Web_page.objects.get_or_create(topic_name=to,name=n,url=u)[0]
        Wo.save()
        return HttpResponse(' data inserted successfully')
    return render(request,'create_webpage.html',d)



def Create_ac(request):
    d={'wo':Web_page.objects.all()}
    if request.method=='POST':
        n=request.POST['name']
        wo=Web_page.objects.get(name=n)
        a=request.POST['author']
        d=request.POST['date']
        ao=Accessrecord.objects.get_or_create(name=wo, author=a, date=d)[0]
        ao.save()
        return HttpResponse('Data Inserted Successfully')
    return render (request,"Create_acessrecord.html",d )

def Acess_record(request):
    d={'Wo':Web_page.objects.all()}
    if request.method=='POST':
        n=request.POST=['name']
        Wo=Web_page.objects.get(name=n)
        a=request.POST['author']
        d=request.POST['date']
        ao=Acess_record.objects.get_or_create(name=Wo,author=a,date=d)[0]
        ao.save()
        return HttpResponse('data inserted succesfullly')
    return render(request,'create_acessrecord.html',d)
        
         