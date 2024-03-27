from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# Create your models here.

class Producto(models.Model):

    idproducto=models.IntegerField()
    nombre = models.CharField(max_length=40)
    precio= models.FloatField()
    stock_critico=models.IntegerField()
    cantdisponible=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre}"
class Cliente(models.Model):

    idcliente=models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    telefono= models.IntegerField()
    mail= models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"{self.nombre}"
    

class Pedido(models.Model):

    numero_pedido=models.IntegerField()
    fecha= models.DateField()
    idproducto=models.IntegerField()
    detalle_producto = models.CharField(max_length=40)
    precio= models.FloatField()
    cantidad=models.IntegerField() 
    monto=models.FloatField()
    def __str__(self) -> str:
        return f"{self.numero_pedido}"
    

class OrdenCompra(models.Model):

    id_orden=models.IntegerField()
    fecha= models.DateField()
    idproducto=models.IntegerField()
    detalle_producto = models.CharField(max_length=40)
    cantidad=models.IntegerField() 
    def __str__(self) -> str:
        return f"{self.id_orden}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")         # Solo guarda la url donde se archivan las avatares. Dentro Carpeta Media 
    user= models.ForeignKey(User,on_delete=models.CASCADE)   # Se elimina el avatar, cuando elimino el user

    def __str__(self) -> str:
        return f"{self.user} {self.imagen}"
      
