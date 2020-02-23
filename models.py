from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Plan(models.Model):
    plantitle=models.CharField( max_length = 255 )
    plandescription=models.TextField()
    
    def __str__(self):
        return self.plantitle
        
    class Meta():
        db_table='plan'
        verbose_name_plural='plans'

class Task(models.Model):
    taskname=models.CharField(max_length=255)
    taskdescription=models.TextField()
    taskdate=models.DateField()
    tasklocation=models.CharField( max_length = 255 )

    def __str__(self):
        return self.firsttaskname
    
    class Meta:
        db_table='firsttask'
        verbose_name_plural='firsttasks'

class Extratask(models.Model):
    extrataskname=models.CharField(max_length=255)
    extrataskdescription=models.TextField()
    thirdtaskdate=models.DateField()
    thirdtasklocation=models.CharField( max_length = 255 )

    def __str__(self):
        return self.extrataskname
    
    class Meta:
        db_table='extratask'
        verbose_name_plural='extratasks'

class Uncompleted(models.Model):
    uncompletedname=models.CharField(max_length=255)
    uncompleteddescription=models.TextField()
    uncompletedchangedate=models.DateField()

    def __str__(self):
        return self.uncompletename
    
    class Meta:
        db_table='uncompleted'

class Completed(models.Model):
    completedtype=models.TextField()

    def __str__(self):
        return self.completeddescription

    class Meta:
        db_table='completed'


