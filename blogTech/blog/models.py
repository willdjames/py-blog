from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.TextField()

    def __str__(self):
        return self.titulo
