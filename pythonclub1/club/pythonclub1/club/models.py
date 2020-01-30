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
    meetdate=models.DateField() 
    meettime=models.TimeField()
    meetlocation=models.CharField( max_length = 255 )
    meetdescription=models.TextField( null = True, blank = True )
    User=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.meetname
    
    class Meta:
        db_table='meet'
        verbose_name_plural='meets'

class Resource(models.Model):
    resourcename=models.CharField(max_length = 255)
    resourceentrydate=models.DateField()
    resourcedescription=models.TextField(null=True, blank=True)
    resourceurl=models.URLField(null = True, blank = True)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Minute(models.Model): 
    minuteattendance=models.ManyToManyField( User )
    minutetime=models.TextField( null = True, blank = False )

    def __str__(self):
        return self.minutetext
    
    class Meta:
        db_table='minute'
        verbose_name_plural='minutes'
    

class Event(models.Model):
    eventname=models.CharField(max_length=255)
    evententrydate=models.DateField()
    eventlocation=models.TextField()
    eventtime=models.TimeField()
    User=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    eventdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.eventname
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'
        
    

    
