from django.db import models

# Create your models here.
class ContactoFeed(models.Model):
	NombreContacto=models.CharField(max_length=128, unique=True)
	TrabajoContacto=models.CharField(max_length=128, unique=True)
	CorreoContacto=models.CharField(max_length=128, unique=True)
	WebContacto=models.CharField(max_length=128, unique=True)
	MensajeContacto=models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.ContactoFeed