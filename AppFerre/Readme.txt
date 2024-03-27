README PROYECTO APLICACIÓN FERRETERIA PELLE

Usuario Prueba
Nombre:     Fernando
Contarseña: coder_456

1) Descripción Proyecto: Aplicación Ferretería Pelle
-Definición Proyecto: La finalidad del proyecto, es desarrollar un “Aplicación” que
facilite la gestión de un comercio minorista, dedicado a la comercialización de
productos de ferretería.
El proyecto se enfoca en los siguientes aspectos:
i) El proceso de solicitud de mercadería por parte de un cliente.
ii) En facilitar la consulta de un producto. En especial sus atributos, por
ejemplo: precio, cantidad disponible, etc.
iii) La emisión de un reporte denominado “stock crítico”; el cual nos permite
saber de manera actualizada, cuales productos son los que se debería solicitar                                        su reposición.                                
Estructura:
Desde la página inicio se pueden acceder a las categorías y acciones.
Acciones: Se accede únicamente desde el primer “widget” que se encuentra a la
derecha de la página principal. Acciones disponibles:
i) Generar un Pedido
ii) Consultar un Producto
iii) Emitir Reporte Stock Mínimo
iv) Generar una Orden de Compra
v) Agregar un Cliente
vi) Agregar un Producto

Categorías: Se puede acceder desde la barra de navegación o desde los comandos
de acceso rápido que se encuentran a la derecha. Se detallan las categorías
disponibles:
i) Productos
ii) Clientes
iii) Pedidos
iv) Ordenes Compra




2) DESCRIPCIÓN DE LOS MODELOS  
Cada categoría   representa un modelo del proyecto, se realiza una breve descripción de cada modelo:
I) Productos: Representa todos los productos del negocio. Sus atributos son;
    A)	 Id Producto: Identificación única del producto que comercializa el negocio.
    B)	Nombre: Descripción del producto en cuestión
    C)	Cantidad Disponible: Cantidad disponible para la venta del producto en cuestión
    D)	Stock Critico: Nivel Stock del producto que una vez alcanzado, se deberá gestionar su compra. 
 II) Clientes: Representa los clientes del negocio. Atributos 
    A)	Id Cliente: Identificación única representado por el CUIT de la persona
    B)	Nombre: Nombre de la Persona
    C)	Apellido: Apellido de la persona
    D)	Mai: Mail de la persona

III)Pedidos: Representa la solicitud de mercadería por parte del cliente a un staff del negocio. Atributos
    A)	ID Pedido: Representa el número de pedido. Cada pedido cuenta con un solo número de pedido
    B)	ID Producto: Id del producto solicitado por el cliente
    C)	Nombre: Nombre característico del producto
    D)	Precio: Precio del producto
    E)	Cantidad: Cantidad solicitada del producto 
III) Ordenes Compra: Representa la solicitud de mercadería por parte del negocio a un proveedor determinado. 
    A)	ID Orden Compra: Representa el número de orden de compra Cada orden cuenta con un solo número de identificación
    B)	ID Producto: Id del producto solicitado 
    C)	Nombre: Nombre característico del producto
    D)	Stock Crítico: Cantidad crítica del producto, por la cual, una vez alcanzada se deberá gestionar la compra
    E)	Cantidad: Cantidad a solicitar del producto en cuestión


  

