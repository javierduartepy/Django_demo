from django.contrib import admin
from .models import Articulo, Clientes, Pedidos, DetallePedidos

# Register your models here.


class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_filter = ("nombre", "seccion")


admin.site.register(Articulo, ArticuloAdmin)


class ClientesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("nombre", "direccion", "email", "telefono")
    search_fields = ("nombre", "direccion", "email", "telefono")


admin.site.register(Clientes, ClientesAdmin)


class PedidosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_filter = ("fecha",)
    list_display = ("entrega", "nro_pedido", "fecha")
    date_hierarchy = "fecha"


admin.site.register(Pedidos, PedidosAdmin)


class DetallePedidosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(DetallePedidos, DetallePedidosAdmin)
