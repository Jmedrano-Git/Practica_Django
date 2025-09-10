from django.db import models

# Create your models here.
class EventosDB(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    lugar = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class OrganizadoresDB(models.Model):
    evento = models.ForeignKey(EventosDB, on_delete=models.CASCADE, related_name="organizadores")
    nombre = models.CharField(max_length=100)
    contacto = models.EmailField(unique=50)

    def __str__(self):
        return self.nombre

