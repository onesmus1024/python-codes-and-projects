from django.http import response
from django.test import SimpleTestCase,Client
from django.urls import reverse,resolve

class TestViews(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.index_url=reverse("api:index")

    def test_indexview(self):
        response=self.client.get(self.index_url)
        self.assertEqual(response.status_code,200)
