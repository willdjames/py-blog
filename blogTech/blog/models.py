from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.TextField()
    autor = models.TextField()
    conteudo = models.TextField()
    data_criacao = models.TextField()
    data_atualizacao = models.TextField()

    def __str__(self):
        return self.titulo
