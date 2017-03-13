from django.db import models

class Producto(models.Model):
	fecha = models.DateTimeField(auto_now=True)
	remesa = models.CharField(max_length=255)
	pedido = models.CharField(max_length=255)
	isbn = models.DecimalField(max_digits=13, decimal_places=0)
	codigoImprenta = models.CharField(max_length=255)
	nombre = models.CharField(max_length=255)
	apellido1 = models.CharField(max_length=255)
	apellido2 = models.CharField(max_length=255)
	nombreCompleto = models.CharField(max_length=255)
	direcc = models.CharField(max_length=255)
	cp = models.DecimalField(max_digits=5, decimal_places=0)
	poblacion = models.CharField(max_length=255)
	provincia = models.CharField(max_length=255)
	telefono = models.DecimalField(max_digits=9, decimal_places=0)
	movil = models.DecimalField(max_digits=9, decimal_places=0)

	def __str__(self):
		return self.pedido