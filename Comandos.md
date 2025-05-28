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

- Apos criar um APP precisamos adicionar ele em settings na paz raiz do projeto.

# Fazendo migration
```
py .\manage.py migrate
```

# Gerando super usuario
```
py .\manage.py createsuperuser
```

# Configurando banco de dados

- Comando utilizado para criar um novo model
```
py .\manage.py makemigrations
```
```
py .\manage.py migrate 
```