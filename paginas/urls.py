# paginas/urls.py
from django.urls import path
from .views import vista_acerca_de, vista_inicio

urlpatterns = [
    path("", vista_inicio, name="inicio"),
    path("acerca-de/", vista_acerca_de, name="acerca_de"),
]
