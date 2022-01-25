from django.urls import reverse,resolve
from django.test import SimpleTestCase
from api.views import index

class TestUrl(SimpleTestCase):
    def setUp(self):
        self.indexurl=reverse('api:index')

    def test_index_url(self):
        self.assertEqual(resolve(self.indexurl).func,index)


