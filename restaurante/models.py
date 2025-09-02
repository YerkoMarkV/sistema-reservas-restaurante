from django.db import models

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    personas = models.IntegerField()
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha} {self.hora}"

# Create your models here.
