from django import forms
from .models import Meet, Resource, Minute, Event

class MeetForm(forms.ModelForm):
    class Meta:
        model=Meet
        fields= '__all__'

