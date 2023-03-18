from django.db import models


class Elevadores(models.Model):
    elevador = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    

    def __str__(self):
        return self.elevador
