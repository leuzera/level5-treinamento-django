# Level 5 - Treinamento Django

## [Em atualização]
## O ambiente de desenvolvimento:
  Neste Treinamento iremos criar uma API RESTful que fará um  [CRUD](https://pt.wikipedia.org/wiki/CRUD) de Pessoas. Antes de mais nada, vamos criar uma pasta chamada ``djangorest``, esta irá armazenar todos os arquivos do nosso projeto.

### Virtual Env:

  Primeiramente, devemos configurar o ``virtualenv`` para que possamos trabalhar um ambiente isolado do sistema, sem interferir em outras aplicações. Para isto, rodamos os seguintes comandos:

Linux:
  - ``virtualenv -p /usr/local/bin/python3 venv``
  - ``source venv/bin/activate``

Windows:
  - ``virtualenv venv``
  - ``venv\Scripts\activate``

Você deve ver um ``(venv)`` no terminal/prompt. Agora que já temos o ambiente de desenvolvimento configurado, podemos começar a instalar as dependências.

### Instalar o Django:
  Django é o framework que nos irá permitir desenvolvermos rapidamente uma aplicação web.

  ``pip install Django``
### Gerar os arquivos básicos:
  O Django já cuida da criação de todo o conteúdo básico do nosso projeto, bastando apenas rodar o seguinte comando:

``django-admin startproject djangorest``

  Devemos ter uma pasta chamada ``djangorest`` criada com a seguinte estrutura:

  ```
  djangorest
  ├── djangorest
  │   ├── __init__.py
  │   ├── __pycache__
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── manage.py

  ```

  Um dos arquivos gerados é o ``manage.py``, este possui os comandos que serão usados para gerenciar nosso projeto, rodar testes, realizar migrações, etc.


### Instalar o DRF:
``pip install djangorestframework``

  DRF é o framework para Django que permite criar uma [API RESTful](https://pt.stackoverflow.com/a/45787).
### Cria os arquivos básicos para uma aplicação Django (api/blog/site):

  Agora podemos criar a nossa aplicação que será utilizada pelo Django, no nosso caso uma API, podendo ser também um site, blog ou o que sua imaginação permitir.

``python3 manage.py startapp api``

  Sua pasta deve estar assim:

```
djangorest
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── djangorest
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

  Para podermos usar nossa ``api`` precisamos registrar ela nas configurações do Django. Fazemos isso editando o arquivo ``djangorest/settings.py``.
  ``` python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'rest_framework', #Adicione estas  
      'api', # duas linhas
  ]
  ```
  Podemos começar a editar os arquivos que foram gerados.

## ``Códigos``
  Já podemos criar nosso banco de dados que armazenará os dados das Pessoas. Como estamos seguindo o TDD, definiremos os teste antes. Vamos editar o arquivo ``api/test.py``

  ``` python
  from django.test import TestCase
  from .models import Pessoas

  class ModelTestCase(TestCase):
      """Esta classe define a suite de testes para o modelo de pessoas"""

      def setUp(self):
          """Define o teste e outras variáveis"""
          self.pessoa_nome = "José"
          self.pessoa = Pessoa(nome=self.pessoa_nome)

      def teste_consegue_criar_uma_pessoa(self):
          """Testa se o modelo de pessoas consegue criar uma Pessoa"""
          old_count = Pessoa.objects.count()
          self.bucketlist.save()
          new_count = Pessoa.objects.count()
          self.assertNotEqual(old_count, new_count)
  ```

  E criaremos um modelo para Pessoa no arquivo ``api/models.py``

  ```python
from django.db import models

class Pessoa(models.Model):
    pass
  ```

  Para rodar os testes, executamos o seguinte comando:

``python3 manage.py test``

  Obviamente teremos um erro, já que nem o modelo nem a classe Pessoa foram criados propriamente.

### Cria os arquivos e realiza a migração do BD:

Modelar um Banco de Dados usando Django é muito simples, não precisando escrever uma unica linha de SQL. Em ``api/models.py`` nos faremos a modelagem.

```python
from django.db import models

class Pessoa(models.Model):
    """Esta classe representa o modelo de Pessoa."""
    nome = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        """Retorna um formato que fácil de se ler"""
        return "{}".format(self.name)
```

Criaremos os arquivos para a migração:

``python3 manage.py makemigrations``

E faremos a migração:

``python3 manage.py migrate``

Rodando o teste novamente veremos que ele será concluído com sucesso e agora possuímos um BD pronto para ser usado.

## Serializers

Serializers irão converter as iformação do BD para JSON e vice-versa, isso facilita a leitura e escrita de dados no nosso sistema. Iremos criar então uma classe ModelSerializer, que ficara responsável por essa conversão. Crie o arquivo ``api/serializer.py`` e coloque o seguinte codigo:

```python
from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    """Serializer para mapear o Modelo para um JSON"""

    class Meta:
        """Classe Meta para mapear os campos do serializer com os campos do modelo"""
        model = Pessoa
        fields = ('id', 'nome')
```
## Views

Vamos criar as views para nossa API. Elas devem lidar com as seguintes funcionalidades:

- Criar uma Pessoa (POST)
- Ler uma Pessoa (GET)
- Atualizar uma Pessoa (PUT)
- Apagar uma Pessoa (DELETE)

Mas antes iremos criar nosso teste. Voltando à ``api/test.py``, adicionamos as seguintes linhas:

```python
# No topo do arquivo
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Após o ModelTestCase
class ViewTestCase(TestCase):
    """Suite de testes para a View da API."""

    def setUp(self):
        """Define o cliente de teste e outras variavéis."""
        self.client = APIClient()
        self.pessoa_dado = {'nome': 'João'}
        self.response = self.client.post(
            reverse('create'),
            self.pessoa_dado,
            format="json")

    def teste_api_pode_criar_uma_pessoa(self):
        """Testa se a API consegue criar uma Pessoa."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
```
Após rodar o teste novamente, veremos que ele irá falhar já que a viwe ainda não foi criada. No arquivo ``api/view.py`` adicionamos:

```python
from rest_framework import generics
from .serializers import PessoaSerializer
from .models import Pessoa

class CreateView(generics.ListCreateAPIView):
    """Define o comportamento de criação da nossa API."""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
```

##URLs

Para finalizar, precisar tratar as URLs de acesso a nossa API. Para isso crie o arquivo ``api/urls.py`` com o seguinte codigo:

```python
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    url(r'^pessoa/$', CreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
```
E no arquivo ``djangorest/urls.py``:

```python
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls')) # Adicione esta linha
]
```

## Rodando o servidor

Com o comando abaixo podemos rodar nosso servidor Django

``python3 manage.py runserver``

Entrando na url http://127.0.0.1:8000/pessoa você deve ter acesso a API criada.

#Lendo, Atualizando e Apagando

No arquivo ``api/views.py`` adicione o codigo:

```python
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Lida com os metódos GET, PUT e DELETE do HTTP"""

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
```
E atualizamos o ``api/urls.py`` para:

```python
from .views import DetailsView

url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
```

Agora você pode acessar as pessoas criadas a partir da url http://127.0.0.1:8000/pessoa/1/ 
## Links utéis
### Tutoriais:
Build a REST API with Django – A Test Driven Approach [Parte 1](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1)
e [Parte 2](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2) (inglês)

[Tutorial Django Girls](https://tutorial.djangogirls.org/pt/) (português)

[Django Web Framework - MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) (inglês)
### TDD (testes):
[A Guide to Testing in Django](toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/) (inglês)
### DRF (Django Rest Framework):
[Django Rest Framework - Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/) (inglês)
### Outros:
Pip:

  - Ubuntu: ``apt install python-pip``
  - Outros sistemas: [Script](https://pip.pypa.io/en/stable/installing/)

Virtualenv:
  - Ubuntu: ``apt install virtualenv``
  - Outros sistemas: [Script](https://virtualenv.pypa.io/en/stable/)

[Piores praticas REST](https://jacobian.org/writing/rest-worst-practices/) (inglês)
