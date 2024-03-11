
from django.urls import path, include
from AppFerre.views import *

urlpatterns = [
   #__________________________________Principal
    path('',home,name="home"),
    path('productos/',producto,name="producto"),
    path('clientes/' ,cliente,name="cliente"),
    path('pedido/'  ,pedido,name="pedido"),
    path('orden_compra/',orden_compra,name="orden_compra"),
    path('fecha_hoy/',fecha_hoy, name ="fecha_hoy"),
    path('stock_critico/',stock_critico, name ="stock_critico"),



   
   #__________________________________Formularios

    path('productoform/',producto_form,name ="productoform"),
    path('clienteform/',cliente_form, name ="clienteform"),
    path('pedidoform/',pedido_form, name ="pedidoform"),
    path('orden_compraform/',ordencompra_form, name ="orden_compraform"),

   
   #__________________________________Buscar
   path('buscar_producto/',BuscarProducto, name ="buscar_producto"),
   path('encontar_producto/',encontrarProducto, name ="encontrar_producto"),


]
