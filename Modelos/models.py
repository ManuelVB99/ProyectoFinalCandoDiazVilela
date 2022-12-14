from django.db import models
from django.contrib.auth.models import User 

class BlogsSalta(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blogsalta', null = True, blank = True)

class BlogsRioNegro(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blogrionegro', null = True, blank = True)

class BlogsMendoza(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blogmendoza', null = True, blank = True)

class BlogsBuenosAires(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blogbuenosaires', null = True, blank = True)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)
# Create your models here.
