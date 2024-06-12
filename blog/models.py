from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
  
