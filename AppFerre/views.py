from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.

from AppFerre.models import *
from AppFerre.forms  import  *



#___________________________Principal: Home (Index)________________________________
def home(request):
    return render(request,"AppFerre/index.html")


#___________________________Productos 

def producto(request):
    contexto={'producto': Producto.objects.all().order_by("idproducto")}
    return render(request,"AppFerre/producto.html",contexto)


#___________________________Clientes 
def cliente(request):
    contexto={'cliente':Cliente.objects.all().order_by("idcliente")}
    return render(request,"AppFerre/cliente.html",contexto)


#___________________________Pedidos 
def pedido(request):
    contexto={'pedido':Pedido.objects.all().order_by("numero_pedido")}
    return render(request,"AppFerre/pedido.html",contexto)


#___________________________Orden Compra 
def orden_compra(request):
    contexto={'orden_compra':OrdenCompra.objects.all().order_by("id_orden")}
    return render(request,"AppFerre/orden_compra.html",contexto)


#_________________________Fecha hoy
def fecha_hoy(request):
    hoy=datetime.datetime.now()
    return render (request,hoy)

#_________________________Stock Crítico
def stock_critico(request):
    contexto={'producto': Producto.objects.all().order_by("idproducto")}
    return render (request,"AppFerre/stock_critico.html",contexto)



#___________________________Formularios ___________________________________________

##__________________________Formulario: Producto___________________________________
def producto_form(request):
    if request.method == "POST":

        form=ProductoForm(request.POST)
        
        if form.is_valid():
            producto_id       =  form.cleaned_data.get("id_producto")
            producto_nombre   =  form.cleaned_data.get("nombre")
            producto_precio   =  form.cleaned_data.get("precio")
            producto_stock    =  form.cleaned_data.get("stock_critico")
            producto_cantdispo=  form.cleaned_data.get("cantdisponible")

            producto = Producto(idproducto=producto_id,nombre=producto_nombre,
                                precio=producto_precio,stock_critico=producto_stock,
                               cantdisponible=producto_cantdispo)
            producto.save()
            return render(request,"AppFerre/producto.html")
    else:
        form= ProductoForm()
    
    return render(request,"AppFerre/productoForm.html",{"formulario":form} )    

##__________________________Formulario: Cliente_______________________________________
def cliente_form(request):

    if request.method == "POST":

        form = ClienteForm(request.POST)
        
        if form.is_valid():
            cliente_id         =  form.cleaned_data.get("idcliente")
            cliente_nombre     =  form.cleaned_data.get("nombre")
            cliente_apellido   =  form.cleaned_data.get("apellido")
            cliente_telefono   =  form.cleaned_data.get("telefono")
            cliente_mail       =  form.cleaned_data.get("mail")
           
            cliente = Cliente(idcliente=cliente_id,nombre=cliente_nombre,apellido=cliente_apellido,
                               telefono=cliente_telefono,mail=cliente_mail)
            cliente.save()
            return render(request,"AppFerre/cliente.html")
    else:
        form= ClienteForm()
    
    return render(request,"AppFerre/clienteForm.html",{"formulario":form} ) 

##__________________________Formulario: Pedido_______________________________________
def pedido_form(request):

    if request.method == "POST":

        form = PedidoForm(request.POST)
        
        if form.is_valid():
            pedido_id          =  form.cleaned_data.get("numero_pedido")
            pedido_fecha       =  form.cleaned_data.get("fecha")
            pedido_idproducto  =  form.cleaned_data.get("idproducto")
            pedido_detalleprod =  form.cleaned_data.get("detalle_producto")
            pedido_precio      =  form.cleaned_data.get("precio")
            pedido_cantidad    =  form.cleaned_data.get("cantidad")
            pedido_monto       =  pedido_precio * pedido_cantidad
            
            pedido = Pedido(numero_pedido=pedido_id,fecha=pedido_fecha,idproducto=pedido_idproducto,
                             detalle_producto=pedido_detalleprod,precio=pedido_precio,
                             cantidad=pedido_cantidad,monto=pedido_monto)
            pedido.save()
            return render(request,"AppFerre/pedido.html")
    else:
        form= PedidoForm()
    
    return render(request,"AppFerre/pedidoForm.html",{"formulario":form} ) 

##__________________________Formulario: Orden Compra_______________________________________
def ordencompra_form(request):

    if request.method == "POST":

        form = OrdenCompraForm(request.POST)
        
        if form.is_valid():
            orden_id          =  form.cleaned_data.get("id_orden")
            orden_fecha       =  form.cleaned_data.get("fecha")
            orden_idproducto  =  form.cleaned_data.get("idproducto")
            orden_detalleprod =  form.cleaned_data.get("detalle_producto")
            orden_cantidad    =  form.cleaned_data.get("cantidad")
            
            
            orden_compra = OrdenCompra(id_orden=orden_id,fecha=orden_fecha,idproducto=orden_idproducto,
                                       detalle_producto=orden_detalleprod,cantidad=orden_cantidad)
            orden_compra.save()
           
            return render(request,"AppFerre/orden_compra.html")
    else:
        form= OrdenCompraForm()
    
    return render(request,"AppFerre/orden_compraForm.html",{"formulario":form} ) 


#___________________________Buscar ___________________________________________

def BuscarProducto(request):
    return render(request,"AppFerre/buscar.html")

def encontrarProducto(request): 
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        producto=Producto.objects.filter(nombre__icontains=patron)
        contexto={"producto":producto}
        return render(request,"AppFerre/producto.html",contexto)
    
    contexto={'producto': Producto.objects.all().order_by("idproducto")}
    return render(request,"AppFerre/producto.html",contexto)
    

