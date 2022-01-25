from django.test import TestCase
from api.models import Task

class TestModel(TestCase):
    def setUp(self):

        self.task=Task.objects.create(name="this is my first task",completed=True)

    def test_task(self):
        self.assertEqual(self.task.completed,True)
        