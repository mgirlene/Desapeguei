from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def test_form_valid(self):
        request = self.client.get(reverse_lazy('index'))
        self.assertEquals(request.status_code, 200)