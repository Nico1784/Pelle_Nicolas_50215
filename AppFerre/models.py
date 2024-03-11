from django.db import models

# Create your models here.
# Create your models here.

class Producto(models.Model):

    idproducto=models.IntegerField()
    nombre = models.CharField(max_length=40)
    precio= models.FloatField()
    stock_critico=models.IntegerField()
    cantdisponible=models.IntegerField()

class Cliente(models.Model):

    idcliente=models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    telefono= models.IntegerField()
    mail= models.CharField(max_length=40)
    

class Pedido(models.Model):

    numero_pedido=models.IntegerField()
    fecha= models.DateField()
    idproducto=models.IntegerField()
    detalle_producto = models.CharField(max_length=40)
    precio= models.FloatField()
    cantidad=models.IntegerField() 
    monto=models.FloatField()

class OrdenCompra(models.Model):

    id_orden=models.IntegerField()
    fecha= models.DateField()
    idproducto=models.IntegerField()
    detalle_producto = models.CharField(max_length=40)
    cantidad=models.IntegerField() 
    
    
