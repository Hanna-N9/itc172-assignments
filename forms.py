from django import forms
from .models import Plan, Task, Extratask, Uncompleted, Completed

class PlanForm(forms.ModelForm):
    class Meta:
        model=Plan
        fields= '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields= '__all__'
    
class ExtrataskForm(forms.ModelForm):
    class Meta:
        model=Extratask
        fields= '__all__'

class UncompletedForm(forms.ModelForm):
    class Meta:
        model=Uncompleted
        fields= '__all__'

class CompletedForm(forms.ModelForm):
    class Meta:
        model=Completed
        fields= '__all__'