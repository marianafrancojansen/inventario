from django import forms
from contacto.models import ContactoFeed

class ContactoFeedForm(forms.ModelForm):

	NombreContacto=forms.CharField(max_length=128)
	TrabajoContacto=forms.CharField(max_length=128)
	CorreoContacto=forms.CharField(max_length=128)
	WebContacto=forms.CharField(max_length=128)
	MensajeContacto=forms.CharField(max_length=128)

	class Meta:
		model = ContactoFeed

		


