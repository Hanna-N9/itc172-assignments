from django.contrib import admin
from .models import Plan, Task, Extratask, Uncompleted, Completed

# Register your models here.
admin.site.register(Plan)
admin.site.register(Task)
admin.site.register(Extratask)
admin.site.register(Uncompleted)
admin.site.register(Completed)
