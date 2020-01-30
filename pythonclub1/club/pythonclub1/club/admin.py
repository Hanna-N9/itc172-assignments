from django.contrib import admin

from django.contrib import admin
from .models import MeetType, Meet, Resource, Minute, Event

# Register your models here.
admin.site.register(MeetType)
admin.site.register(Meet)
admin.site.register(Resource)
admin.site.register(Minute)
admin.site.register(Event)