from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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

class RegistroForm(UserCreationForm):
    
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)  ## widget: funciona para que no se vea la contraseña cuando escribo
    password2= forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User  # Hace que el usuario ingesado se grabe en la table user de la B.D. 
        fields = ["username","email","password1","password2"]   # Campos que quiero que se vea en el form 

class UserEditForm(UserChangeForm):   # Form, que me permite que EL usuario edite ssu datos  
    
    email= forms.EmailField(required=True)
    first_name= forms.CharField(label="Nombre/s", max_length=40, required=True)   
    last_name=  forms.CharField(label="Apellido/s", max_length=40, required=True)   
    class Meta:    
        model= User  #Vincula con la tabla usurio 
        fields = ["email","first_name","last_name"]   # Campos que quiero que se vea en el form 


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True) 


   