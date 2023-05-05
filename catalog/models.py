from django.db import models


class Dirname(models.Model):
    objects = None
    name = models.CharField(max_length=64, help_text='pon el nombre del director')

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    objects = None
    namePelicula = models.CharField(max_length=64)
    sumary = models.TextField(max_length=300, help_text='Resumen pelicula')
    Dirname = models.ManyToManyField(Dirname)

    def __str__(self):
        return self.namePelicula


