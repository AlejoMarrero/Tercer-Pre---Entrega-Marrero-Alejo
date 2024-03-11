from django.db import models

class Producto(models.Model):
    modelo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100)
    cuit = models.CharField(max_length=20, unique=True)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateField(auto_now_add=True)

class Venta(models.Model):
    cliente = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateField(auto_now_add=True)
