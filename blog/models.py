from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    resumen = models.CharField(max_length=500)
    contenido = models.CharField(max_length=3000)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to="post", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, titulo:{self.titulo}, autor:{self.autor}"
