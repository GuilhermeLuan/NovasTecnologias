# Django
- Ambiente virtual Django
- https://docs.djangoproject.com/en/5.1/howto/windows/

# Install
```
py -m venv .venv
.venv\Scripts\activate
py -m pip install Django
```

# Criando projeto
```
django-admin startproject project
```

# Rodando o projeto
```
py manage.py runserver
```

# Criando um APP
```
py .\manage.py startapp app
```
- Sempre que criamos um APP novo devemos registrar ele no `settings.py`

# Banco de dados

- Fazer migrate do banco de dados
```
py manage.py migrate
```
- Criar um superuser
```
py manage.py createsuperuser
```