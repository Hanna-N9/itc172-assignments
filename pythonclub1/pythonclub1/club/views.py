from django.shortcuts import render, get_object_or_404
from .models import MeetType

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

    from .models import MeetType, Meet, Event, Resource, Minute

def gettypes(request):
    type_list=MeetType.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})

def getmeet(request):
    meet_list=MeetType.objects.all()
    return render(request, 'club/meet.html' ,{'meet_list' : meet_list})

def meetDetail(request, id):
    m=Meet.objects.get_object_or_404(Product, pk=id)
    resource=Resource.objects.filter(meet=id)
    context={
     'm' : m,
        'resourcecount' : resourcecount,
        'resource' : resource,
    }
    return render(request, 'club/meetdetail.html', context=context)