from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
	list_display = ('remesa','pedido', 'isbn', 'nombreCompleto','direcc', 'cp', 'poblacion', 'provincia', 'telefono', 'movil',)
	#list_filter = ('remesa','pedido', 'isbn', 'nombreCompleto','direcc', 'cp', 'poblacion', 'provincia',)
