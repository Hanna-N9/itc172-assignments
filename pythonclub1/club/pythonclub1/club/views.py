from django.shortcuts import render, get_object_or_404
from .models import MeetType, Meet, Event, Resource, Minute


# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getresource(request):
    resource_list = Resource.objects.all()
    return render( request, 'club/resources.html', {'resource_list' : resource_list})

def gettypes(request):
    type_list=MeetType.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})

def getmeet(request):
    meet_list=Meet.objects.all()
    return render(request, 'club/meet.html' ,{'meet_list' : meet_list})

def meetDetail(request, id):
    meet=Meet.objects.get_object_or_404(Product, pk=id)
    return render(request, 'club/meetdetail.html',{'detail' : detail})
    resources=Resource.objects.filter(meet=id)
    context={
     'meet' : meet,
        'resource' : resource,
    }
    return render(request, 'club/meetdetail.html', context=context)