from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def transaccion(request):
    if(request.method == "POST"):
        transa = formTransaccion(request.POST)
        if transa.is_valid():
            transa.save()
            return redirect(to=transaccion)
    else:
        transa = formTransaccion()
    return render(request, 'core/transaccion.html',{'form':transa})

def reportes(request):
    return render(request, 'core/reportes.html')

def historial(request):
    return render(request, 'core/historial.html')