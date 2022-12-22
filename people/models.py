from django.db import models

# Create your models here.
class People(models.Model):
    # Atributos
    name = models.CharField(max_length=100)

    # To String
    def __str__(self):
        return self.name
