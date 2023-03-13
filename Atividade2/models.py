from django.db import models


class Elevadores(models.Model):
    preferido = models.CharField(max_length=200)
    periodo = models.CharField(max_length=255)

    def __str__(self):
        return self.preferido
