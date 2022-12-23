from django.db import models

# Create your models here.
class People(models.Model):
    # Atributos
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,null=True)

    # To String
    def __str__(self):
        return self.name + " (" + self.email + ")"


class Service(models.Model):
    service = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    date = models.DateField
    client = models.ForeignKey(People, on_delete=models.CASCADE)
    value = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.service
