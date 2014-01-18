from django.db import models

# Create your models here.

class MapaFeed(models.Model):
	NombreMapa=models.CharField(max_length=128, unique=True)
	TrabajoMapa=models.CharField(max_length=128, unique=True)
	CorreoMapa=models.CharField(max_length=128, unique=True)
	WebMapa=models.CharField(max_length=128, unique=True)
	MensajeMapa=models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.MapaFeed

