from django import forms

class ProductoForm(forms.Form):
    id_producto= forms.IntegerField(required=True)
    nombre= forms.CharField(max_length=40, required=True)
    precio= forms.FloatField(required=True)
    stock_critico= forms.IntegerField(required=True)
    cantdisponible= forms.IntegerField(required=True)


class ClienteForm(forms.Form):
    idcliente=forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    telefono= forms.IntegerField()
    mail= forms.CharField(max_length=40)
    

class PedidoForm(forms.Form):
    numero_pedido=forms.IntegerField()
    fecha= forms.DateField()
    idproducto=forms.IntegerField()
    detalle_producto = forms.CharField(max_length=40)
    precio= forms.FloatField()
    cantidad=forms.IntegerField()
    
class OrdenCompraForm(forms.Form):
    id_orden=forms.IntegerField()
    fecha= forms.DateField()
    idproducto=forms.IntegerField()
    detalle_producto = forms.CharField(max_length=40)
    cantidad=forms.IntegerField() 
   