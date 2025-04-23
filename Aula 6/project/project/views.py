from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contato(request):
    return HttpResponse(
        """
        <p> Contato </p>
        <ul>    
            <li> guilherme@gmail.com</li>
            <li> 11 99999-9999</li>
        </ul>
        """
    )