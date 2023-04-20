from django.db import models

# Create your models here.

class Paises(models.Model):
    nome = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome