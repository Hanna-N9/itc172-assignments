from django.shortcuts import render, get_object_or_404
from .models import MeetType, Meet, Event, Resource, Minute
from .forms import MeetForm
from django.contrib.auth.decorators import login_required

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

#Create loginmessage and logoutmessage views

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')

@login_required
def newMeet(request):
     form=MeetForm
     if request.method=='POST':
          form=MeetForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetForm()
     else:
          form=MeetForm()
     return render(request, 'club/newmeet.html', {'form': form})

def neResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'club/newmeet.html', {'form': form})

def newMinute(request):
     form=MinuteForm
     if request.method=='POST':
          form=MinuteForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MinuteForm()
     else:
          form=MinuteForm()
     return render(request, 'club/newmeet.html', {'form': form})



    