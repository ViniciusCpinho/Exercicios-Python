from django.db import models


class Pagamento(models.Model):
    nome = models.CharField(max_length=255)
    quantidade_horas = models.FloatField(max_length=10000)
    turno = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    valorTotal = models.FloatField(max_length=10000)
    valorHora = models.FloatField(max_length=10000)

    def __str__(self):
        return self.nome
