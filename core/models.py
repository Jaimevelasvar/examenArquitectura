from django.db import models
from datetime import datetime
class Ropa(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.tipo

class Transaccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    destino = models.CharField(max_length=100)
    ropa = models.CharField(max_length=20, default='')
    cantidad = models.IntegerField()
    tipo_transaccion = models.CharField(max_length=10)
    estado_ropa = models.CharField(max_length=10)
    fecha = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return "Transaccion "+str(self.id)