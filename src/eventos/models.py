from django.db import models

# Create your models here.
class EventosDB(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    lugar = models.CharField(max_length=50)

