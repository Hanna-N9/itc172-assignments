from django.shortcuts import render
from .models import Plan, Task, Extratask, Uncompleted, Completed


# Create your views here.
def index(request):
    return render(request, 'agenda/index.html')

def getplan(request):
    plan_list = Plan.objects.all()
    return render( request, 'agenda/plan.html', {'plan_list' : plan_list})

def gettask(request):
    task_list = Meeting.objects.all()
    return render( request, 'agenda/task.html', {'task_list' : task_list})

def getextratask(request):
    extratask_list = MeetingMinutes.objects.all()
    return render( request, 'agenda/extratask.html', {'extratask_list' : extratask_list})

def getuncompleted(request):
    uncompleted_list = Event.objects.all()
    return render( request, 'agenda/uncompleted.html', {'uncompleted_list' : uncompleted_list})

def getcompleted(request):
    completed_list = Event.objects.all()
    return render( request, 'agenda/completed.html', {'completed_list' : completed_list})



#Create loginmessage and logoutmessage views

def loginmessage(request):
    return render(request, 'agenda/loginmessage.html')

def logoutmessage(request):
    return render(request, 'agenda/logoutmessage.html')

@login_required
def newPlan(request):
     form=PlanForm
     if request.method=='POST':
          form=PlanForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=PlanForm()
     else:
          form=PlanForm()
     return render(request, 'agenda/newplan.html', {'form': form})

def newTask(request):
     form=TaskForm
     if request.method=='POST':
          form=TaskForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TaskForm()
     else:
          form=TaskForm()
     return render(request, 'agenda/newplan.html', {'form': form})

def newExtraTasks(request):
     form=MinuteForm
     if request.method=='POST':
          form=ExtrataskForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ExtrataskForm()
     else:
          form=MinuteForm()
     return render(request, 'agenda/newplan.html', {'form': form})

def newUncompleted(request):
     form=UncompletedForm
     if request.method=='POST':
          form=UncompletedForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=UncompletedForm()
     else:
          form=UncompletedForm()
     return render(request, 'agenda/newplan.html', {'form': form})

def newCompleted(request):
     form=CompletedForm
     if request.method=='POST':
          form=CompletedForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=CompletedForm()
     else:
          form=CompletedForm()
     return render(request, 'agenda/newplan.html', {'form': form})


