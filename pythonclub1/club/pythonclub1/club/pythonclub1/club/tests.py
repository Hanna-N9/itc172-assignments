from django.test import TestCase
from django.urls import reverse
from .models import Meet, Resource, Minute, Event
from django.contrib.auth.models import User

# Create your tests here.clear

class MeetTest(TestCase):
    def test_stringOutput(self):
        meeting= Meet(meetname= 'School Meeting')
        self.assertEqual(str(meeting), meeting.meetname)
    
    def test_tablename(self):
        self.assertEqual(str(Meet._meta.db_table), 'meet')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        res=Resource(resourcename='Training')
        self.assertEqual(str(resource), res.resourcename)
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')
    
class EventTest(TestCase):
    def test_stringOutput(self):
        ev=Event(eventname='Improvement is Fun Event')
        self.assertEqual(str(event), ev.eventname)
        
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class MinuteTest(TestCase):
    def test_stringOutput(self):
        minu=Minute(minutetime='50')

#test for models
class MeetTestModel(TestCase):
    def setup(self):
        self.u=user.objects.create(username='myuser')
        meeting=Meet.objects.create(meetname = "School Meeting", meetdate = "2020-09-09", meettime = "9:00", meetlocation = "Seattle Central College", meetdescription = "Attend for descriptions")
        return meet
    
    def test_string(self):
        self.assertEqual(str(self.meeting),self.meeting.meetname)
    
    def test_string(self):
        self.assertEqual(str(self.meeting),self.meeting.meetdate)
    
    def test_string(self):
        self.assertEqual(str(self.meeting),self.meeting.meettime)
    
    def test_string(self):
        self.assertEqual(str(self.meeting),self.meeting.meetlocation)
    
    def test_string(self):
        self.assertEqual(str(self.meeting),self.meeting.meetdescription)
    
    def test_tablename(self):
        self.assertEqual(str(Minute._meta.db_table), 'minute')

# Test for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class MeetTestView(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myuser')
        meeting=Meet.objects.create(meetname = "School Meeting", meetdate = "2020-09-09", meettime = "9:00", meetlocation = "Seattle Central College", meetdescription = "Attend for descriptions")
        return meet
        
class ResourceTestView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('resource')
        self.assertEqual(response.status_code, 200)

class MinuteTestView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('minute')
        self.assertEqual(response.status_code, 200)

class EventResourceView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('event')
        self.assertEqual(response.status_code, 200)
    
    def test_meet_detail_success(self):
        meeting=self.setup()
        response = self.client.get(reverse("meetdetail", args=(self.meeting.id,)))
        self.assertEqual(response.status_code, 200)

#form tests
class New_Meet_Form_Test(TestCase):
    def test_meetform_is_valid(self):
        form=MeetForm(data={'meetname' : "School Meeting", 'meetdate' : "2020-09-09", 'meettime' : "9:00", 'meetlocation' : "Seattle Central College", 'meetdescription' : "Attend for descriptions" })
        self.assertTrue(form.is_valid())
    
    def test_meetform_invalid(self):
        form=meetform(data={'meetname' : "School Meeting", 'meetdate' : "2020-09-09", 'meettime' : "9:00", 'meetlocation' : "Seattle Central College", 'meetdescription' : "Attend for descriptions" })
        self.assertFalse(form.is_valid())
        
    def test_meetform_empty(self):
        form=meetform(data={'meetname' : "School Meeting", 'meetdate' : "2020-09-09", 'meettime' : "9:00", 'meetlocation' : "Seattle Central College", 'meetdescription' : "Attend for descriptions" })
        self.assertFalse(form.is_valid())
