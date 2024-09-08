Vou começar a montar a apostila passo a passo, seguindo a estrutura sugerida. Aqui está o início da apostila com os primeiros capítulos explicados em detalhes:

---

# **Apostila Django - Do Básico ao Profissional**

## Capítulo 1: Introdução ao Django

### O que é Django?
Django é um framework web escrito em Python que permite o desenvolvimento rápido de aplicativos web seguros e escaláveis. Ele segue o princípio do "batteries included", o que significa que ele já vem com muitas funcionalidades essenciais integradas, como autenticação, roteamento de URLs, banco de dados, administração, e muito mais.

**Principais características do Django:**
- **Segurança:** Protege contra vulnerabilidades comuns como injeção de SQL, CSRF, e XSS.
- **Escalabilidade:** Utilizado em projetos de grande escala como Instagram e Pinterest.
- **Produtividade:** Django fornece uma maneira rápida de criar aplicações web completas, incluindo painel de administração e autenticação de usuários.

### Instalando e configurando o Django

#### 1. Instalando Python
Para usar o Django, é necessário ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

Para verificar se o Python está instalado corretamente, abra o terminal ou prompt de comando e digite:
```bash
python --version
```
Isso deve retornar a versão do Python.

#### 2. Instalando o Django
Com o Python instalado, o próximo passo é instalar o Django. O gerenciador de pacotes `pip`, que já vem com o Python, será utilizado para isso. No terminal ou prompt de comando, execute o seguinte comando:
```bash
pip install django
```

#### 3. Criando um projeto Django
Após instalar o Django, vamos criar o primeiro projeto Django. Execute o seguinte comando para criar um novo projeto:
```bash
django-admin startproject nome_do_projeto
```
Isso criará uma nova pasta com o nome do projeto e a estrutura básica do Django.

#### 4. Estrutura básica de um projeto Django
Aqui está a estrutura padrão de um projeto Django:
```
nome_do_projeto/
    manage.py
    nome_do_projeto/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- **manage.py:** Um script que facilita a execução de comandos relacionados ao Django, como iniciar o servidor ou criar migrations.
- **settings.py:** Arquivo de configuração principal do Django.
- **urls.py:** Onde são definidos os roteamentos de URLs.
- **wsgi.py e asgi.py:** Arquivos relacionados à interface do servidor web com a aplicação Django.

#### 5. Iniciando o servidor de desenvolvimento
Para ver a aplicação rodando, inicie o servidor de desenvolvimento do Django:
```bash
python manage.py runserver
```
Você poderá acessar a aplicação no navegador em `http://127.0.0.1:8000/`.

---

## Capítulo 2: Criando sua Primeira Aplicação Django

### O que é uma aplicação no Django?
No Django, um projeto pode ser composto por várias **aplicações**. Cada aplicação é responsável por uma funcionalidade específica. Por exemplo, você pode ter uma aplicação para blog, outra para o sistema de usuários e outra para e-commerce, tudo dentro do mesmo projeto.

### Criando uma aplicação Django
Dentro do seu projeto, você pode criar uma aplicação rodando o seguinte comando:
```bash
python manage.py startapp nome_da_aplicacao
```
Isso criará uma nova pasta com a estrutura da aplicação, como mostrado abaixo:
```
nome_da_aplicacao/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

### Estrutura de uma aplicação Django
- **models.py:** Onde você define as classes que correspondem às tabelas do banco de dados.
- **views.py:** Contém as funções que respondem às requisições dos usuários.
- **admin.py:** Configura o que aparecerá no painel de administração.
- **migrations/**: Armazena arquivos de migrações para o banco de dados.

### Configurando a aplicação no projeto
Para ativar a nova aplicação no projeto, você precisa adicioná-la no arquivo `settings.py`. Abra o arquivo e localize a lista `INSTALLED_APPS`. Adicione a sua aplicação à lista assim:
```python
INSTALLED_APPS = [
    ...
    'nome_da_aplicacao',
]
```

---

## Capítulo 3: Trabalhando com Views, URLs e Templates

### Criando Views
As **views** no Django são funções ou classes que recebem uma solicitação do navegador e retornam uma resposta, que geralmente é uma página HTML.

Vamos criar uma view simples no arquivo `views.py` da sua aplicação:
```python
from django.http import HttpResponse

def minha_primeira_view(request):
    return HttpResponse("Olá, Django!")
```

### Configurando URLs
Para que a view criada possa ser acessada pelo navegador, precisamos mapear uma URL para ela. Isso é feito no arquivo `urls.py` da aplicação. Crie o arquivo `urls.py` dentro da sua aplicação e adicione o seguinte:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.minha_primeira_view),
]
```

Depois, você precisa incluir as URLs da aplicação no arquivo `urls.py` principal do projeto:
```python
from django.urls import include, path

urlpatterns = [
    path('minha_app/', include('nome_da_aplicacao.urls')),
]
```

Agora, ao acessar `http://127.0.0.1:8000/minha_app/`, você verá a mensagem "Olá, Django!".

### Trabalhando com Templates
Os **templates** no Django são arquivos HTML que podem conter variáveis e lógica básica para renderizar páginas dinâmicas.

Crie uma pasta chamada `templates` dentro da sua aplicação e crie um arquivo `index.html` dentro dessa pasta:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha primeira página Django</title>
</head>
<body>
    <h1>{{ mensagem }}</h1>
</body>
</html>
```

Modifique a view para renderizar esse template:
```python
from django.shortcuts import render

def minha_primeira_view(request):
    return render(request, 'index.html', {'mensagem': 'Olá, Django com Templates!'})
```

Agora, ao acessar a mesma URL, você verá a mensagem renderizada pelo template.

---

## Capítulo 4: Modelos e Banco de Dados

### O que são modelos no Django?
Os **modelos** no Django são classes que representam tabelas do banco de dados. Cada atributo da classe corresponde a uma coluna na tabela.

Crie um modelo simples no arquivo `models.py` da sua aplicação:
```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
```

### Criando Migrations
Migrations são a maneira como o Django aplica as alterações nos modelos ao banco de dados. Para criar e aplicar migrations, use os comandos:
```bash
python manage.py makemigrations
python manage.py migrate
```

Isso criará a tabela `Produto` no banco de dados.

### Usando o painel de administração
Para gerenciar seus modelos via painel de administração, registre-os no arquivo `admin.py`:
```python
from django.contrib import admin
from .models import Produto

admin.site.register(Produto)
```

Agora, você pode acessar `http://127.0.0.1:8000/admin/`, logar com seu usuário de superadmin e gerenciar os produtos.

---

## Capítulo 5: Formulários e Validações

### Criando formulários no Django
No Django, os formulários são usados para capturar dados de entrada dos usuários. Eles podem ser criados manualmente ou usando a classe `Form`.

Vamos criar um formulário simples em `forms.py` para capturar o nome e preço de um produto:
```python
from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    preco = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2)
```

### Exibindo o formulário em um template
Na view, renderize o formulário em um template para que os usuários possam preenchê-lo:
```python
from django.shortcuts import render
from .forms import ProdutoForm

def produto_view(request):
    form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})
```

No arquivo `produto_form.html`, exiba o formulário:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enviar</button>
</form>
```

### Processando os dados enviados pelo usuário
Ao submeter o formulário, os dados precisam ser validados e processados. Modifique a view para lidar com as submissões:
```python
def produto_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            preco = form.cleaned_data['preco']
            # Aqui você pode salvar os dados no banco de dados
            return HttpResponse(f'Produto {nome} cadastrado com sucesso!')
    else:
        form = ProdutoForm()

    return render(request, 'produto_form.html', {'form': form})
```

### Validações
O Django faz a validação automática com base nos tipos de campos que você define no formulário. Se houver erros de validação, o Django exibe as mensagens no template. O método `is_valid()` verifica se os dados estão corretos.

---

## Capítulo 6: Autenticação e Autorização

### Sistema de autenticação do Django
O Django possui um sistema de autenticação embutido que facilita o gerenciamento de usuários, logins e permissões.

#### Criando um sistema de login
Primeiro, vamos criar um formulário de login simples:
```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse('Login realizado com sucesso!')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
```

No template `login.html`:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```

### Logout
Para fazer logout do usuário, use a função `logout` do Django:
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponse('Você saiu com sucesso!')
```

### Protegendo rotas com login obrigatório
Para garantir que apenas usuários autenticados possam acessar determinadas views, use o decorador `login_required`:
```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return HttpResponse('Bem-vindo ao dashboard!')
```

---

## Capítulo 7: Trabalhando com Arquivos Estáticos e Media

### Servindo arquivos estáticos
Os arquivos estáticos, como CSS e JavaScript, são usados para estilizar e adicionar interatividade às páginas.

Para configurar arquivos estáticos, adicione um diretório `static/` na sua aplicação e configure o caminho no `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

Nos templates, use a tag `static` para incluir arquivos CSS ou JS:
```html
<link rel="stylesheet" href="{% static 'css/estilos.css' %}">
```

### Trabalhando com arquivos de mídia
Se sua aplicação lida com upload de arquivos, você precisa configurar um diretório para armazená-los. No `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Upload de arquivos no formulário
Para capturar uploads de arquivos, adicione um campo de arquivo no formulário:
```python
class UploadForm(forms.Form):
    arquivo = forms.FileField()
```

No template:
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enviar</button>
</form>
```

Na view, processe o upload:
```python
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            # Salvar o arquivo ou processá-lo
            return HttpResponse('Upload realizado com sucesso!')
    else:
        form = UploadForm()

    return render(request, 'upload_form.html', {'form': form})
```

---

## Capítulo 8: Testes Automatizados

### Introdução a testes no Django
Testes automatizados são fundamentais para garantir a qualidade do código. O Django fornece uma estrutura robusta para testes.

Para criar um teste básico, edite o arquivo `tests.py` na sua aplicação:
```python
from django.test import TestCase
from .models import Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(nome="Produto Teste", preco=10.0)

    def test_produto(self):
        produto = Produto.objects.get(nome="Produto Teste")
        self.assertEqual(produto.preco, 10.0)
```

### Executando testes
Para rodar os testes, utilize o seguinte comando:
```bash
python manage.py test
```

### Testando views e formulários
Você também pode testar as views e a submissão de formulários:
```python
from django.test import Client

def test_form_view(self):
    c = Client()
    response = c.post('/minha_app/', {'nome': 'Novo Produto', 'preco': '25.0'})
    self.assertEqual(response.status_code, 200)
```

---

## Capítulo 9: Implantação de uma Aplicação Django

### Preparando a aplicação para produção
Antes de implantar sua aplicação, algumas configurações precisam ser ajustadas. No `settings.py`, certifique-se de definir:
- **DEBUG = False**
- **ALLOWED_HOSTS** com os domínios autorizados:
```python
ALLOWED_HOSTS = ['meusite.com', 'www.meusite.com']
```

### Configuração de arquivos estáticos
Para produção, os arquivos estáticos precisam ser coletados e servidos corretamente:
```bash
python manage.py collectstatic
```

### Usando Nginx e Gunicorn
Gunicorn é um servidor WSGI que roda a aplicação Django. O Nginx pode ser configurado para servir os arquivos estáticos e rotear as requisições para o Gunicorn.

1. Instale o Gunicorn:
```bash
pip install gunicorn
```
2. Execute o Gunicorn:
```bash
gunicorn nome_do_projeto.wsgi
```

3. Configure o Nginx para rotear as requisições.

### Deploy em plataformas como Heroku
Se preferir utilizar plataformas como Heroku, siga as instruções de configuração disponíveis na [documentação oficial](https://devcenter.heroku.com/articles/getting-started-with-django).

---

## Capítulo 10: Conclusão e Próximos Passos

### Resumo do que foi aprendido
Ao longo desta apostila, você aprendeu os conceitos básicos e intermediários do Django, incluindo:
- Configuração inicial do projeto e aplicações
- Criação de views, URLs e templates
- Uso de modelos para interação com o banco de dados
- Trabalhando com formulários, autenticação e uploads
- Testes automatizados e preparação para produção

### Desafios e projetos sugeridos
Para continuar aprendendo, recomendo que você crie projetos práticos, como:
- Um blog simples com cadastro de posts e sistema de comentários
- Um sistema de e-commerce com cadastro de produtos e carrinho de compras

### Recursos adicionais
- [Documentação oficial do Django](https://docs.djangoproject.com)
- Comunidades online como StackOverflow e Django Fórum

---
