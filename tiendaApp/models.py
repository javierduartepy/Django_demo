from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.CharField(max_length=100)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'clientes'
        verbose_name = 'cliente'
        ordering = ['created']

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    seccion = models.CharField(max_length=50, default=None)
    precio = models.FloatField(default=None)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'articulos'
        verbose_name = 'articulo'
        ordering = ['created']

    def __str__(self):
        return 'El nombre es %s la Seccion es %s y el precio es %s' % (
            self.nombre,
            self.seccion,
            self.precio
        )


class Pedidos(models.Model):
    nro_pedido = models.IntegerField()
    fecha = models.DateField(max_length=80)
    entrega = models.BooleanField()
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        ordering = ['created']

    def __int__(self):
        return self.nro_pedidos


class DetallePedidos(models.Model):
    detallePedido = models.ForeignKey(
        Pedidos, on_delete=models.RESTRICT, related_name="detallePedido")
    detalleArticulo = models.ForeignKey(
        Articulo, on_delete=models.RESTRICT, related_name="detalleArticulo")
    cantidad = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'detalles'
        verbose_name = 'detalle'
        ordering = ['created']

    def __str__(self):
        return self.cantidad
