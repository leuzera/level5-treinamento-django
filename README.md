# Level 5 - Treinamento Django

## [Em atualização]
## O ambiente de desenvolvimento:

  Vamos criar uma pasta chamada ``djangorest``, esta irá armazenar todos os arquivos do nosso projeto.

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
``pip install Django``

  Django é o framework que nos irá permitir desenvolvermos rapidamente uma aplicação web.
### Gerar os arquivos básicos:
  O Django já cuida da criação de todo o conteúdo básico do nosso projeto, bastando apenas rodar o seguinte comando:

``django-admin startproject djangorest``

  Devemos ter uma pasta chamada ``djangorest`` criada com a seguinte estrutura:

  ```
    djangorest
    ├─djangorest
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
  ```

  Um dos arquivos gerados é o ``manage.py``, este possui os comandos que serão usados para gerenciar nosso projeto, rodar testes, realizar migrações, etc.


### Instalar o DRF:
``pip install djangorestframework``

  DRF é o framework para Django que permite criar uma [API RESTful](https://pt.stackoverflow.com/a/45787).
### Cria os arquivos básicos para uma aplicação Django (api/blog/site):

  Agora podemos criar a nossa aplicação que será utilizada pelo Django, no nosso caso uma API, podendo ser também um site, blog ou o que sua imaginação permitir.

``python3 manage.py startapp api``

  Podemos começar a editar os arquivos que foram gerados.

## ``Códigos``

### Roda os teste:
``python3 manage.py test``
### Cria os arquivos e realiza a migração do BD:
``python3 manage.py makemigrations``

``python3 manage.py migrate``

### Tutorial rápido:
Build a REST API with Django – A Test Driven Approach [Parte 1](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1)
[Parte 2](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2) (inglês)
### Tutorial completo:
[Tutorial Django Girls](https://tutorial.djangogirls.org/pt/) (português)

[Django Web Framework - MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) (inglês)
### TDD (testes):
[A Guide to Testing in Django](toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/) (inglês)
### DRF (Django Rest Framework):
[Django Rest Framework - Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/) (inglês)
### Outros:
Pip:

  - Ubuntu: ``apt install python-pip``
  - Outros: [Script](https://pip.pypa.io/en/stable/installing/)

[Django](https://www.djangoproject.com/) (inglês)

Virtualenv:
  - Ubuntu: ``apt install virtualenv``
  - Outros: [Script](https://virtualenv.pypa.io/en/stable/)

[Piores praticas REST](https://jacobian.org/writing/rest-worst-practices/) (inglês)
