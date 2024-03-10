from django.db import models

class Consulente(models.Model):
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return self.nome

