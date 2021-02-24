from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.TextField()
    autor = models.TextField()
    conteudo = models.TextField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()
    categoria = models.TextField()

    def __str__(self):
        return self.titulo
