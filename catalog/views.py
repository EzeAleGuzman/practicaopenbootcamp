
from django.shortcuts import render
from .models import Dirname, Pelicula

def index(request):
    directores = Dirname.objects.all()
    peliculas = Pelicula.objects.all()
    resumen = [p.sumary for p in peliculas]

    return render(request, 'index.html', {'directores': directores, 'peliculas': peliculas, 'resumen': resumen})