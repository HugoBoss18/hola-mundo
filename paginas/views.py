from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vista_inicio(request):
    return HttpResponse("Hello, World!")


def vista_acerca_de(request):
    return HttpResponse("Página Acerca de")
