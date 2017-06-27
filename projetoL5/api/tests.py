from django.test import TestCase
from .models import Bucketlist

class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = "Escreve algo"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_pode_criar_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


