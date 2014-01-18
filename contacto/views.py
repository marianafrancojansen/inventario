from django.shortcuts import render
from django.template import RequestContext

from contacto.forms import ContactoFeedForm

# Create your views here.
def index(request):
	return render(request , 'contacto.html')

def gracias(request):
	# context = RequestContext(request)

	if request.method == 'POST':
		form = ContactoFeedForm(request.POST)

		if form.is_valid():
			formClean = form.cleaned_data
			form.save(commit=True)
			context = {}
			for key, value in formClean.iteritems():
				context[key] = value
			print context
			return render(request, 'gracias.html', context)

		else:
			print 'not valid'
			print form.errors
	else:
		print 'else'
		form = ContactoFeedForm()

		


	return render(request , 'gracias.html', form)
