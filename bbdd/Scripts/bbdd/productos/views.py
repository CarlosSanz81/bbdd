from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

def hello_world(request):
	#return HttpResponse ('hola')
	product = Producto.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'productos': Producto
	}
	return HttpResponse(template.render(context, request))

# Create your views here.
