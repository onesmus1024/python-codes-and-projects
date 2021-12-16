from django.test import TestCase

# Create your tests here.
class test1(TestCase):
    def foo(self):
        self.assertIs('foo'.upper(),'FOfO')