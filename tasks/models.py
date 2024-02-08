from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted  = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '-by' + self.user.username
    

class Compus(models.Model):
    marca = models.CharField(max_length=50)
    serial= models.CharField(max_length=20)
    descricion=models.TextField(blank=True)
    hora_inicio = models.DateTimeField(null=True, blank=True)
    hora_fin = models.DateTimeField(null=True, blank=True)


class Aprendiz(models.Model):
    Nombre = models.CharField(max_length=200)
    Documento = models.IntegerField(null=True, blank=True)
    Formacion = models.CharField(max_length=300)
    Ficha = models.IntegerField(null=True, blank=True)
    
