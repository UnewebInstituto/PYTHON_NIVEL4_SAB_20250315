from django.db import models

class contactos(models.Model):
  nombre   = models.CharField(max_length=250)
  apellido = models.CharField(max_length=255)
  correo   = models.CharField(max_length=255, unique = True)
  telefono = models.CharField(max_length=255)

#
def __str__(self):
  return f"{self.nombre} {self.apellido} {self.correo} {self.telefono}"
