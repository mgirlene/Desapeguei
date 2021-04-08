from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def test_list(self):
        request = self.client.get(reverse_lazy('index'))
        self.assertEquals(request.status_code, 200)