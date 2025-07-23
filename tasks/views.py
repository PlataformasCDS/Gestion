from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.


def home(request):
    title = "hello World"
    # return HttpResponse('<h1> Hello Wordl </h1>')
    return render(request, 'home.html')

def alumno(request):
    return render(request, 'alumno.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return HttpResponse('Usuario creado e iniciado sesión')
        else:
            return render(request, 'signup.html', {
                'form': form,
                'error': 'Corrige los errores del formulario'
            })
