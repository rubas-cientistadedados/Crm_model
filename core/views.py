from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logaut as app_logaut

def login(request):
    return render(request, "login.html")

def submit_login(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user:
            django_login(request, user)
            return redirect("index")
        else:
           messages.error(request, "Usuário/Senha inválida") 

    return redirect("login")

def logaut(request):
    app_logaut(request)
    return redirect('login')