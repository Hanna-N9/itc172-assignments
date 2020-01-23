from django.shortcuts import render 
from .models import MeetType

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

    from .models import MeetType, Meet, Event, Resource, Minute

def gettypes(request):
    type_list=MeetType.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})
