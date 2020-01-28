from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MeetType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.typename
    
    class Meta:
         db_table='MeetType'
         verbose_name_plural='MeetTypes'

class Meet(models.Model):
    meetname=models.CharField(max_length=255)
    meetentrydate=models.DateField() 
    meetlocation=models.TextField()
    meettime=models.TextField()
    User=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    meetdescription=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.meetname
    
    class Meta:
        db_table='meet'
        verbose_name_plural='meet'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourceentrydate=models.DateField() 
    User=models.ManyToManyField(User)
    resourceid=models.ForeignKey(Meet, on_delete=models.CASCADE)
    resourceurl=models.URLField(null=True, blank=True)
    resourcetype=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Minute(models.Model): 
    minutename=models.CharField(max_length=255)
    minuteid=models.ForeignKey(Meet, on_delete=models.CASCADE)
    User=models.ManyToManyField(User)
    minuteattendance=models.ManyToManyField
    minutetext=models.TextField()

    def __str__(self):
        return self.minutename
    
    class Meta:
        db_table='minute'
        verbose_name_plural='minutes'
    

class Event(models.Model):
    eventname=models.CharField(max_length=255)
    evententrydate=models.DateField()
    eventlocation=models.TextField()
    eventtime =models.TextField()
    User=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    eventdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.eventname
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'
        
    

    
