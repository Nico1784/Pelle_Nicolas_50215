from django.shortcuts import render,redirect
import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from AppFerre.models import *
from AppFerre.forms  import *


##___________________________PRINCIPAL: Home (Index)_____________________________________
def home(request):
    return render(request,"AppFerre/index.html")

##________________________  STOCK CRITICO _________________________________________________
@login_required
def stock_critico(request):
    contexto={'producto': Producto.objects.all().order_by("idproducto")}
    return render (request,"AppFerre/stock_critico.html",contexto)

##__________________________   PRODUCTO   ___________________________________________________

class ProductoList(LoginRequiredMixin,ListView):
     model= Producto
     
class ProductoCreate(LoginRequiredMixin,CreateView):
    model=Producto
    fields=['idproducto','nombre','precio','stock_critico','cantdisponible']
    success_url= reverse_lazy("productos")

class ProductoUpdate(LoginRequiredMixin,UpdateView):
    model=Producto
    fields=['idproducto','nombre','precio','stock_critico','cantdisponible']
    success_url= reverse_lazy("productos")

class ProductoDelete(LoginRequiredMixin,DeleteView):
    model=Producto
    success_url= reverse_lazy("productos")

#_____________________________  CLIENTE  ____________________________________________________

class ClienteList(LoginRequiredMixin,ListView):
     model= Cliente
     
class ClienteCreate(LoginRequiredMixin,CreateView):
    model=Cliente
    fields=['idcliente','nombre','apellido','telefono','mail']
    success_url= reverse_lazy("clientes")

class ClienteUpdate(LoginRequiredMixin,UpdateView):
    model=Cliente
    fields=['idcliente','nombre','apellido','telefono','mail']
    success_url= reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model=Cliente
    success_url= reverse_lazy("clientes")


#_____________________________  PEDIDOS  ________________________________________________________

class PedidoList(LoginRequiredMixin,ListView):
     model= Pedido
     
class PedidoCreate(LoginRequiredMixin,CreateView):
    model=Pedido
    fields=['numero_pedido','fecha','idproducto','detalle_producto','precio',  
            'cantidad', 'monto' ]
    success_url= reverse_lazy("pedidos")

class PedidoUpdate(LoginRequiredMixin,UpdateView):
    model=Pedido
    fields=['numero_pedido','fecha','idproducto','detalle_producto','precio',
            'cantidad','monto']
    success_url= reverse_lazy("pedidos")

class PedidoDelete(LoginRequiredMixin,DeleteView):
    model=Pedido
    success_url= reverse_lazy("pedidos")


#____________________________  ORDEN COMPRA  _________________________________________________________

class OrdenCompraList(LoginRequiredMixin,ListView):
     model= OrdenCompra
     
class OrdenCompraCreate(LoginRequiredMixin,CreateView):
    model=OrdenCompra
    fields=['id_orden','fecha','idproducto','detalle_producto','cantidad']
    success_url= reverse_lazy("orden_compras")

class OrdenCompraUpdate(LoginRequiredMixin,UpdateView):
    model=OrdenCompra
    fields=['id_orden','fecha','idproducto','detalle_producto','cantidad']
    success_url= reverse_lazy("orden_compras")

class OrdenCompraDelete(LoginRequiredMixin,DeleteView):
    model=OrdenCompra
    success_url= reverse_lazy("orden_compras")



#___________________________  BUSCAR PRODUCTO  __________________________________________________________
@login_required
def BuscarProducto(request):
    return render(request,"AppFerre/buscar.html")

@login_required
def encontrarProducto(request):
     request.GET["buscar"]
     patron= request.GET["buscar"]

     if len (Producto.objects.filter(nombre__icontains=patron))>0:

        patron= request.GET["buscar"]
        Producto.objects.filter(nombre__icontains=patron)
        producto=Producto.objects.filter(nombre__icontains=patron)
        contexto={"producto_list":producto}
        return render(request,"AppFerre/producto_list.html",contexto)
     
     else:
        texto="PRODUCTO NO ENCONTRADO!"
        contexto={'texto':texto }
        return render (request,"AppFerre/producto_no_encontrado.html",contexto)
        

##____________________________   LOG IN    ___________________________________________________________________

def login_request(request):
    if request.method == "POST":                    ## Entra por segunda vez con las datos cargados en el form
        usuario  =  request.POST["username"]
        clave    =  request.POST["password"]
        user = authenticate(username=usuario,password=clave )
        texto="DATOS INGRESADOS INCORRECTOS, INTENTE NUEVAMENTE"
        contexto={'texto':texto}
        

        if user is not None:        ## Formula que me autentica el usuario
                login (request,user)
                #__Avatar
                try:
                    avatar= Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar= "/media/avatares/default.png"
                finally: 
                    request.session["avatar"]= avatar

                return render(request, "AppFerre/index.html" )
        else:
                 texto="DATOS INGRESADOS INCORRECTOS "
                 contexto={'texto':texto}
                 return render(request, "AppFerre/login_error.html",contexto )
                #return redirect (reverse_lazy('login'))
        
    else:
        miform=AuthenticationForm()    ## Cuando entra por primera vez
                                      
    return render(request,"AppFerre/login.html",{"form":miform} )   


##____________________________   LOG OUT     _______________________________________________________________________

def logoutUser(request):
    logout(request)
    return redirect('home') 

##____________________________   REGISTRO USUARIO     ________________________________________________________________

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "AppFerre/registro.html", {"form": miForm} )  
 
  ##____________________________   EDICIÓN PERFIL CAMBIAR PASSWORD    ___________________________________________________

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "AppFerre/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppFerre/cambiar_clave.html"
    success_url = reverse_lazy("home")

##____________________________  CAMBIO AVATAR   _______________________________________________________________________

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario  = User.objects.get(username = request.user)
            
            avatarviejo = Avatar.objects.filter(user=usuario)
            if len(avatarviejo) > 0:
                for i in range(len(avatarviejo)):
                    avatarviejo[i].delete()
            
            avatar= Avatar(user=usuario ,imagen= miForm.cleaned_data ["imagen"] )

            avatar.save()
            imagen= Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen 
            print(f"{imagen}")
            
            return redirect(reverse_lazy('home'))
    else:
  
        miForm = AvatarForm()

    return render(request, "AppFerre/agregarAvatar.html", {"form": miForm} )  

##____________________________  About Us   _______________________________________________________________________

def about_us(request):
    return render(request,"AppFerre/about_us.html")
