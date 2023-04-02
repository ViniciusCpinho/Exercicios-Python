from django.db import models

class File(models.Model):
    has_file = models.BooleanField(False)
