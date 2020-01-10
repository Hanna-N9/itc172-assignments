from django.urls import path
from . import views

#this is a comment (# is how to comment like IDLE) or <!--This is a comment as well-->

urlpatterns=[
    path('', views.index, name='index'),
]
