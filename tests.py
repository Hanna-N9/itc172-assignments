from django.test import TestCase
from django.urls import reverse
from .models import Plan, Task, Extratask, Uncompleted, Completed
from django.contrib.auth.models import User

# Create your tests here.

class PlanTest(TestCase):
    def test_stringOutput(self):
        planning=plan(plantitle= 'The agenda')
        self.assertEqual(str(plan), plan.plantitle)
    
    def test_tablename(self):
        self.assertEqual(str(Plan._meta.db_table), 'plan')

class TaskTest(TestCase):
    def test_stringOutput(self):
        res=Task(taskname= 'Homeowrk')
        self.assertEqual(str(task), res.taskname)
    
    def test_tablename(self):
        self.assertEqual(str(Task._meta.db_table), 'task')
    
class ExtraTaskTest(TestCase):
    def test_stringOutput(self):
        ev=Extratask(extrataskname='Unrelated school stuffs')
        self.assertEqual(str(extratask), ev.extrataskname)
        
    def test_tablename(self):
        self.assertEqual(str(Extratask._meta.db_table), 'extratask')

class UncompletedTest(TestCase):
    def test_stringOutput(self):
        ev=Uncompleted(uncompletedname='Uncompleted tasks')
        self.assertEqual(str(uncompleted), ev.uncompletedname)
        
    def test_tablename(self):
        self.assertEqual(str(Uncompleted._meta.db_table), 'uncompleted')

class CompletedTest(TestCase):
    def test_stringOutput(self):
        ev=Completed(completedtype='Completed assignment')
        self.assertEqual(str(completed), ev.completedtype)
        
    def test_tablename(self):
        self.assertEqual(str(Completed._meta.db_table), 'completed')

#test for models/views
class PlanTestModel(TestCase):
    def setup(self):
        self.u=user.objects.create(username='myuser')
        plan=Plan.objects.create(plantitle= "The agenda", plandescription= "The to-do list for me to do")
        return plan
    
    def test_string(self):
        self.assertEqual(str(self.plan),self.plan.plantitle)
    
    def test_string(self):
        self.assertEqual(str(self.plan),self.plan.plandescription)
    
    
# Test for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class PlanTestView(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myuser')
        plan=Plan.objects.create(plantitle= "The agenda", plandescription= "The to-do list for me to do")
        return plan
        
class TaskTestView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('task')
        self.assertEqual(response.status_code, 200)

class ExtraTaskTestView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('extratask')
        self.assertEqual(response.status_code, 200)

class UncompletedTestView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('uncompleted')
        self.assertEqual(response.status_code, 200)

class CompletedTestView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get('completed')
        self.assertEqual(response.status_code, 200)

#form tests
class New_Plan_Form_Test(TestCase):
    def test_planform_is_valid(self):
        form=PlanForm(data={'plantitle': "The agenda", 'plandescription': "The to-do list for me to" })
        self.assertTrue(form.is_valid())

