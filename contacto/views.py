from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request , 'contacto.html')

def gracias(request):
	for key, values in request.POST.iteritems():
		print key, values
	return render(request , 'gracias.html')

