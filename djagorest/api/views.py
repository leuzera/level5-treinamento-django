from django.shortcuts import render
from rest_framework import generics
from .serializers import PessoaSerializer
from .models import Pessoa

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Lida com os metódos GET, PUT e DELETE do HTTP"""

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
