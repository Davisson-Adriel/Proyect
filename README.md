# SISTEMA DE GESTIÓN DE INVENTARIOS PANADERIA
El siguiente repositorio hace referencia a un sistema que permite llevar el control del inventario y solicitud de pedidos de una panaderia. Permitiendo registrar productos, agregar pedidos y hacer consultas.
## Instalación (Apertura)
Para la apertura del programa se puede realizar la clonaciòn del repositorio o descargar el archivo comprimido para abrirlo en su dispositivo local sin conectarlo con la nube.
## Uso
El archivo ejecutable principal se encuentra en el archivo main.py. Para poner en marcha el sistema tan solo es necesario ejecutar este archivo desde su plataforma de desarrollo preferida.
#### Menú principal
Una vez ejecutado el archivo main.py el sistema le mostrara el siguiente menú:
```breach
--------------------------------------------------
Bienvenido a Digital Delicias Casera
--------------------------------------------------
 
1. Registro de productos
2. Pedidos
3. Consultas
4. Salir
 
--------------------------------------------------

Digite la opciòn deseada: 
```
#### Registro de productos
Si desea registrar nuevos productos, se debe seleccionar la opción #1. EL sistema desplegara solicitudes al usuario para el ingreso de la información del nuevo producto. El sistema identifica que no se creen productos bajo el mismo codigo. Observará lo siguiente:
```breach
Digite la opciòn deseada: 1
--------------------------------------------------
Registro de nuevo producto
--------------------------------------------------
Digite el codigo del producto
CP-123
Nombre del Producto: Pan Cascarita
--------------------------------------------------
1. Pan
2. Pastel
3. Postre 
--------------------------------------------------
Seleccione la categoria del producto: 1
Descripción del producto: Delicioso pan con cascara crocante
Proovedor: ARADO S.A.S
Cantidad en Stock: 200
Precio de Venta: 500
Precio de Proovedor: 100
--------------------------------------------------
PRODUCTO AGREGADO CON EXITO
--------------------------------------------------
```
### Menú pedidos
Si selecciona la opción #2 el sistema desplegara el submenu pedidos.
```breach
Digite la opciòn deseada: 2
--------------------------------------------------
 
1. Registrar nuevo pedido
2. Visualizar Pedidos
3. Buscar Pedido
4. Editar Pedido
5. Eliminar pedido
6. Salir
 
--------------------------------------------------

Digite la opciòn deseada:
```
### Registro de pedidos
Si desea registrar un nuevo pedido, se debe selccionar la opción #1. El sistema desplegara solicitudes al usuario para el ingreso de la información del nuevo pedido. Al igual que con el registro de productos, el sistema identifica codigos de pedidos ya existentes. Veremos lo siguiente:
```breach
Digite la opciòn deseada: 1
--------------------------------------------------
Registro de nuevo pedido
--------------------------------------------------
Digite el codigo (cedula) del cliente
CC-1665398735
Digite el codigo del pedido
CPE-123
Digite el dia (numerico): 10
Digite el mes (numerico): 02
Digite el año: 2025
Digite el codigo del producto que solicita
CP-001
Digite la cantidad a solicitar: 10
¿Desea agregar otro producto al pedido?
1. SI
2. NO
Digite su elección: 1
--------------------------------------------------
Ingrese la información del nuevo producto
--------------------------------------------------
Digite el codigo del producto que solicita
CP-123
Digite la cantidad a solicitar: 100
¿Desea agregar otro producto al pedido?
1. SI
2. NO
Digite su elección: 2
--------------------------------------------------
Pedido Registrado con Exito
--------------------------------------------------
```
### Visualizar Pedidos
Los pedidos se registrar y se visualizan de la siguiente manera:
```breach
--------------------------------------------------
Pedido--> CPE-123
--------------------------------------------------
Codigo de pedido - CPE-123
Codigo de Cliente - CC-1665398735
Fecha - 2025/2/10
--------------------------------------------------
Detalles del pedido
--------------------------------------------------
Codigo de pedido - CPE-123
Codigo de producto - CP-001
Cantidad - 10
Precio Unidad - 500.0
Numero de Linea - 1
--------------------------------------------------
```
### Buscar pedidos
Mediante la opción #3 el sistema le permite buscar un pedido mediante diferentes identificadores
```breach
Digite la opciòn deseada: 3
--------------------------------------------------
1. Buscar por Codigo
2. Filtrar pedidos por producto
3. Salir
--------------------------------------------------
Digite la opciòn deseada: 
```
Una vez identificado el pedido, se imprime tal cual como en la opción de visualizar pedidos. Si no se encuentra un pedido con base en la informaciòn ingresada, el sistema lo informa.
```breach
Digite el codigo del pedido
CPE-2332
--------------------------------------------------
Pedido no existe
--------------------------------------------------
```
### Editar y eliminar pedido
El sistema permite editar la cantidad o productos ingresados en un pedido, de igual forma permite eliminar pedidos ya existentes.
```breach
Digite la opciòn deseada: 4
Digite el codigo del pedido que desea editar
CPE-123
--------------------------------------------------
A continuación se visualiza la información del pedido
--------------------------------------------------
Codigo de pedido - CPE-123
Codigo de Cliente - CC-1665398735
Fecha - 2025/2/10
--------------------------------------------------
Detalles del pedido
--------------------------------------------------
Codigo de pedido - CPE-123
Codigo de producto - CP-001
Cantidad - 10
Precio Unidad - 500.0
Numero de Linea - 1
--------------------------------------------------
Codigo de pedido - CPE-123
Codigo de producto - CP-123
Cantidad - 100
Precio Unidad - 500.0
Numero de Linea - 1
--------------------------------------------------
1. Cambiar de producto
2. Cambiar la cantidad
3. Cancelar
--------------------------------------------------
Digite de acuerdo a su elección: 
```
Para eliminar observariamos lo siguiente:
```breach
Digite la opciòn deseada: 5
Digite el codigo del pedido que desea eliminar
CPE-123
--------------------------------------------------
Esta seguro de eliminar el pedido:  CPE-123
1. SI
2. NO
--------------------------------------------------
Digite el numero de acuerdo a su elección: 1
Pedido Eliminado exitosamente
--------------------------------------------------
```
### Consultas
Si se selecciona la opción #3 se nos despliega el sisguiente menú:
```breach
Digite la opciòn deseada: 3
--------------------------------------------------
 
1. Buscar Productos
2. Mirar Inventario
3. Salir
 
--------------------------------------------------

Digite la opciòn deseada: 
```
AL igual que con los pedidos tambien podemos buscar productos ingresados en el inventario mediante identificadores.
```breach
Digite la opciòn deseada: 1
--------------------------------------------------
1. Buscar por Nombre
2. Buscar por Categoria
3. Buscar por Codigo
4. Salir
--------------------------------------------------
Digite la opciòn deseada: 
```
Los productos y su información se visualiza de la siguiente manera:
```breach
--------------------------------------------------
Digite la opciòn deseada: 3
--------------------------------------------------
Digite el codigo del producto
CP-001
--------------------------------------------------
Codigo de Producto--> CP-001
--------------------------------------------------
Nombre - Pan cascarita
Categoria - Pan
Descripcion - Pan cascarita crocante
Proovedor - Agrado.SAS
Cantidad en Stock - 90
Precio de venta - 500.0
Precio de Proovedor - 100.0
```
## Lenguajes Integrados
- Python
## Plataforma (s) de Desarrollo
- Visual Studio
## Contacto
- droman819@unab.edu.co
- https://github.com/Davisson-Adriel
## Autor (s)
- Davisson Adriel Roman Carreño
## Estado del proyecto
- Finalizado
## Link del Repositorio
[Nombre del repositorio](https://github.com/Davisson-Adriel/Nombre-del-Repositorio)