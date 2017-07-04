from django.test import TestCase
from .models import Pessoa


class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = "Escreve algo"
        self.bucketlist = Pessoa(name=self.bucketlist_name)

    def test_model_pode_criar_bucketlist(self):
        old_count = Pessoa.objects.count()
        self.bucketlist.save()
        new_count = Pessoa.objects.count()
        self.assertNotEqual(old_count, new_count)
