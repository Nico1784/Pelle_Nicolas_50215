
from django.urls import path, include
from AppFerre.views import *



urlpatterns = [
    #__________________________________INICIO______________________________________
   
    path('',home,name="home"),
    
    #_________________________________PRODUCTOS_____________________________________
    
    path('productos/',ProductoList.as_view(),name="productos"),
    path('create_producto/',ProductoCreate.as_view(),name="create_producto"),
    path('update_producto/<int:pk>/',ProductoUpdate.as_view(),name="update_producto"),
    path('delete_producto/<int:pk>/',ProductoDelete.as_view(),name="delete_producto"),
   

    #_________________________________BUSCAR UN PRODUCTO______________________________

    path('buscar_producto/',BuscarProducto, name ="buscar_producto"),
    path('encontar_producto/',encontrarProducto, name ="encontrar_producto"),
       

    #__________________________________CLIENTES______________________________________

    path('clientes/',ClienteList.as_view(),name="clientes"),
    path('create_cliente/',ClienteCreate.as_view(),name="create_cliente"),
    path('update_cliente/<int:pk>/',ClienteUpdate.as_view(),name="update_cliente"),
    path('delete_cliente/<int:pk>/',ClienteDelete.as_view(),name="delete_cliente"),


    #__________________________________PEDIDO_____________________________________________
    
    path('pedidos/',PedidoList.as_view(),name="pedidos"),
    path('create_pedido/',PedidoCreate.as_view(),name="create_pedido"),
    path('update_pedido/<int:pk>/',PedidoUpdate.as_view(),name="update_pedido"),
    path('delete_pedido/<int:pk>/',PedidoDelete.as_view(),name="delete_pedido"),


   #__________________________________ORDENES COMPRA________________________________________
    
    path('orden_compras/',OrdenCompraList.as_view(),name="orden_compras"),
    path('create_orden_compra/',OrdenCompraCreate.as_view(),name="create_orden_compra"),
    path('update_orden_compra/<int:pk>/',OrdenCompraUpdate.as_view(),name="update_orden_compra"),
    path('delete_orden_compra/<int:pk>/',OrdenCompraDelete.as_view(),name="delete_orden_compra"),

    #__________________________________STOCK CRITICO
    path('stock_critico/',stock_critico, name ="stock_critico"),

    
    #__________________________________ LOGIN  _____________________________________________

    path('login/',login_request, name ="login"),

    #__________________________________ LOGOUT _____________________________________________

    path('logout/',logoutUser, name ="logout"),
    
    #__________________________________ REGISTRO _____________________________________________

    path('registro/',register, name ="registro"),

    #__________________________________ EDICION PERFIL  _______________________________________
  
     path('editarPerfil/',editProfile, name ="editarPerfil"),
     path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    
    #__________________________________ AVATAR  _______________________________________________

     path('agregar_avatar/',agregarAvatar, name ="agregar_avatar"),

     #__________________________________ ABOUT US  _______________________________________________

     path('about_us/',about_us, name ="about_us"),

   ]
