from django import forms
from .models import Meet, Resource, Minute, Event

class MeetForm(forms.ModelForm):
    class Meta:
        model=Meet
        fields= '__all__'
    
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

class MinuteForm(forms.ModelForm):
    class Meta:
        model = Minute
        fields = '__all__'

