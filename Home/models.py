from django.db import models


class Atividades(models.Model):
    nome_Atividade = models.CharField(max_length=256)
    url = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_Atividade
