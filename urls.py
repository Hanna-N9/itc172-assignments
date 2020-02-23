from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getplan/', views.getplan, name='plan'),
    path('gettask/', views.gettask, name='task'),
    path('getextratask/', views.getextratask, name='extratask'),
    path('getuncompleted/', views.getuncompleted, name='uncompleted'),
    path('getcompleted/', views.getcompleted, name='completed'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]


