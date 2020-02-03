

#this is a comment (# is how to comment like IDLE) or <!--This is a comment as well-->

from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getmeet/', views.getmeet, name='meet'),
    path('meetDetail/<int:id>', views.meetDetail, name='meetdetail'),
    path('newMeet/', views.newMeet, name='newmeet'),

]

