productos={}
pedidos={}
det_pedido={}

def mostrar_menu():
    print("--------------------------------------------------")
    print(" ")
    print("1. Registro de productos\n2. Pedidos\n3. Consultas\n4. Salir")
    print(" ")
    print("--------------------------------------------------")
    #Esta función muestra el menú princiapl

def menu_consultas():
    print("--------------------------------------------------")
    print(" ")
    print("1. Buscar Productos\n2. Mirar Inventario\n3. Salir")
    print(" ")
    print("--------------------------------------------------")
    #Muestra las opciones del apartado consultas

def menu_pedidos():
    print("--------------------------------------------------")
    print(" ")
    print("1. Registrar nuevo pedido\n2. Visualizar Pedidos\n3. Buscar Pedido\n4. Editar Pedido\n5. Eliminar pedido\n6. Salir")
    print(" ")
    print("--------------------------------------------------")
    #Muestra el apartado del menú pedidos

def pedir_opc():
    #Solicita al usuario la opción deseada
    print("")
    opc=int(input("Digite la opciòn deseada: "))
    return opc

def ag_producto():
    print("--------------------------------------------------")
    print("Registro de nuevo producto")
    print("--------------------------------------------------")
    
    #Se solicita al usuario que digite el codigo del nuevo producto
    #Para este caso tome la decisión de asignarle un prefijo para que la identificación del producto fuera mas sencilla
    #De esta manera cada producto esta representado idealmente por numeros y se limita la confunción del sistema con otros codigos
    while True:
        print("Digite el codigo del producto")
        cod=input("CP-")
        if cod.isdigit():  
            cod = f"CP-{cod}" 
            break
        else:
            print("--------------------------------------------------")
            print("Ingrese solo numeros")
            print("--------------------------------------------------")
    
    #Se usa la función .isdigit para verificar que el valor ingresado sea unicamente numerico
    #Una vez verificado se concatena el prefijo con el valor ingresado
    #En este punto se usa .get para verificar que el codigo ingresado no exista en la base de datos
    eva=productos.get(cod,1)
    if eva==1:
        
        while True:
            nom=input("Nombre del Producto: ")
            if len(nom)>0:
                break
            else:
                print("No se puede dejar el nombre vacio")
        #Lo que se hace es usar len() para corroborar que no se ingrese un valor vacio
        #Posteriormente entra en un subciclo while true para solicitar la categoria
        #Se usa un menú para limitar errores
        while True:
            try:
                print("--------------------------------------------------")
                print("1. Pan\n2. Pastel\n3. Postre ")
                print("--------------------------------------------------")
                opc=int(input("Seleccione la categoria del producto: "))
                if opc==1:
                    cat="Pan"
                    break
                elif opc==2:
                    cat="Pastel"
                    break
                elif opc==3:
                    cat="Postre"
                    break
                else:
                    print("--------------------------------------------------")
                    print("Opciòn invalida, vuelva a digitar")
            except ValueError:
                print("--------------------------------------------------")
                print("Opciòn invalida (SOLO NUMEROS)")
        #Antes de continuar se verifica que el valor ingresado sea solo numerico y dentro de las opciones posibles
        while True:
            des=input("Descripción del producto: ")
            if len(des)>0:
                break
            else:
                print("No se puede dejar la descripción vacia")
        #Lo que se hace es usar len() para corroborar que no se ingrese un valor vacio
        while True:
            pro=input("Proovedor: ")
            if len(pro)>0:
                break
            else:
                print("No se puede dejar el proovedor vacio")
        #Lo que se hace es usar len() para corroborar que no se ingrese un valor vacio
        while True:
            try:
                cantstock=int(input("Cantidad en Stock: "))
                if cantstock>0:
                    break
                else:
                    print("--------------------------------------------------")
                    print("Valor Invalido, intente nuevamente")
                    print("--------------------------------------------------")

            except ValueError:
                print("--------------------------------------------------")
                print("Opciòn invalida (SOLO NUMEROS)")
                print("--------------------------------------------------")
        #Se evalua que el valor ingresado sea superior a cero, sea un entero y sea numerico
        while True:
            try:
                preventa=float(input("Precio de Venta: "))
                if preventa>0:
                    break
                else:
                    print("--------------------------------------------------")
                    print("Valor Invalido, intente nuevamente")
                    print("--------------------------------------------------")
            except ValueError:
                print("--------------------------------------------------")
                print("Opciòn invalida (SOLO NUMEROS)")
                print("--------------------------------------------------")
        #Se evalua que el valor ingresado sea superior a cero y sea numerico
        while True:
            try:
                prepro=float(input("Precio de Proovedor: "))
                if prepro>0:
                    break
                else:
                    print("--------------------------------------------------")
                    print("Valor Invalido, intente nuevamente")
                    print("--------------------------------------------------")
            except ValueError:
                print("--------------------------------------------------")
                print("Opciòn invalida (SOLO NUMEROS)")
                print("--------------------------------------------------")
        #Se evalua que el valor ingresado sea superior a cero y sea numerico
        codigo={"Nombre":nom,"Categoria":cat,"Descripcion":des,"Proovedor":pro,"Cantidad en Stock":cantstock,"Precio de venta":preventa,"Precio de Proovedor":prepro}
        productos[cod]=codigo
        print("--------------------------------------------------")
        print("PRODUCTO AGREGADO CON EXITO")
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("Codigo de producto ya existente")
        print("--------------------------------------------------")
        #Por ultimo se almacena la información con cada una de sus llaves correspondientes en un diccionario codigo
        #Finalmente se guarda ese diccionario en un diccionario llamado productos bajo la llave codigo

def ag_pedido():
    
    print("--------------------------------------------------")
    print("Registro de nuevo pedido")
    print("--------------------------------------------------")
    #Se solicita la cedula del cliente
    #Se verifica que el valor ingresado sea unicamente numerico con .isdigit
    #Se verifica que sea una cedula valida usando len()
    while True:
        print("Digite el codigo (cedula) del cliente")
        codcliente=input("CC-")
        if codcliente.isdigit():
            if len(codcliente)==10 or len(codcliente)==8:
                codcliente = f"CC-{codcliente}"
                break
            else:
                print("Cedula no Valida")
        else:
            print("--------------------------------------------------")
            print("Ingrese solo numeros")
            print("--------------------------------------------------")
    #Se verifica que el valor ingresado sea unicamente numerico con .isdigit
    while True:  
        while True:
            print("Digite el codigo del pedido")
            codped=input("CPE-")
            if codped.isdigit(): 
                codped = f"CPE-{codped}"  
                break
            else:
                print("--------------------------------------------------")
                print("Ingrese solo numeros")
                print("--------------------------------------------------")
        #Se verifica que el codigo de pedido no exista
        eva=pedidos.get(codped)
        if eva!=None:
            print("Codigo de pedido existente, digite uno nuevo")
        else:
            break
    #Se verifica que sea un valor netamente numerico, en algunos casos el .isdigit se puede sustituir por aprovechando el try
    #Se verifica que el valor corresponda a un dia posible
    while True:
        try:
            dia=int(input("Digite el dia (numerico): "))
            if dia>0 and dia<=30:
                dia=str(dia)
                break
            else:
                print("Dia no valido")
        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS Y ENTEROS)")
            print("--------------------------------------------------")
    #Se verifica que sea un valor netamente numerico, en algunos casos el .isdigit se puede sustituir por aprovechando el try
    #Se verifica que el valor corresponda a un mes posible
    while True:
        try:
            mes=int(input("Digite el mes (numerico): "))
            if mes>0 and mes<=12:
                mes=str(mes)
                break
            else:
                print("Mes no valido")
        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS Y ENTEROS)")
            print("--------------------------------------------------")
    #Se verifica que sea un valor netamente numerico, en algunos casos el .isdigit se puede sustituir por aprovechando el try
    #Se verifica que el valor corresponda a un año igual o superior al actual
    while True:
        try:
            año=int(input("Digite el año: "))
            if año>=2025:
                año=str(año)
                break
            else:
                print("Año no valido")
        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS Y ENTEROS)")
            print("--------------------------------------------------")
    #Se concatena el valor de la fecha en formato Año/mes/dia
    fecha=str(año+"/"+mes+"/"+dia)
    det_pedido[codped]=[]
    #Se da inicio a la solicitud de los detalles del pedido, los cuales se almacenan en el diccionario det_pedido bajo la llave del codigo del pedido
    #En este punto se inicializan varios while true debido a las solicitudes que se realizan
    while True:
        while True:
            while True:
                while True:
                    print("Digite el codigo del producto que solicita")
                    codpro=input("CP-")
                    if codpro.isdigit():  
                        codpro = f"CP-{codpro}" 
                        break
                    else:
                        print("Ingrese solo numeros")
                
                eva=productos.get(codpro)
                #Se verifica valor unicamente numerico y que exista el codigo de producto
                if eva==None:
                    print("Codigo de producto inexistente, intente nuevamente")
                    break
                else:  
                    if productos[codpro]["Cantidad en Stock"] <= 0:
                        print("Producto agotado, no se puede realizar el pedido")
                        print("--------------------------------------------------")
                        #Se verifica la cantidad en stock de dicho producto
                        #Cancela el pedido
                        break
                    else:
                        while True:
                            
                            while True:
                                try:
                                    cant=int(input("Digite la cantidad a solicitar: "))
                                    #Se solicita la cantidad que se desea
                                    #Se verifica que no sea un valor nulo o invalido
                                    if cant>0:
                                        break
                                    else:
                                        print("--------------------------------------------------")
                                        print("Valor Invalido, intente nuevamente")
                                        print("--------------------------------------------------")

                                except ValueError:
                                    print("--------------------------------------------------")
                                    print("Opciòn invalida (SOLO NUMEROS)")
                                    print("--------------------------------------------------")
                            #Se verifica que la cantidad solicitada no supere la cantidad en stock
                            if ((productos[codpro]["Cantidad en Stock"])-cant)<0:
                                print("Imposible solicitar dicha cantidad, digite una nueva")
                            else:
                                #Se actualiza el inventario de dicho producto
                                productos[codpro]["Cantidad en Stock"]=productos[codpro]["Cantidad en Stock"]-cant
                                break
                #Se almancenan los detalles dle pedido en un dicionario llamado detalle
                #Se almacena detalles en el diccionario det_pedido bajo la llave codped que es el codigo del pedido
                #Se alamcena la informacion del pedido en el diccionario pedidos, el cual en la llave "Detalles del pedido"
                #Tiene como valor la información alamcenada en el diccionario det_pedido[codped]
                detalles={"Codigo de pedido":codped,"Codigo de producto":codpro,"Cantidad":cant,"Precio Unidad":productos[codpro]["Precio de venta"],"Numero de Linea":1}
                det_pedido[codped].append(detalles)
                pedidos[codped]={"Codigo de pedido":codped,"Codigo de Cliente":codcliente,"Fecha":fecha,"Detalles del pedido":det_pedido[codped]}
                #Se crea la alerta si la cantidad en stock del producto solicitado es inferior a cinco
                if productos[codpro]["Cantidad en Stock"]<5:
                    print("--------------------------------------------------")
                    print("ALERTA: SOLO RESTAN ", productos[codpro]["Cantidad en Stock"] ," UNIDADES DE",productos[codpro]["Nombre"])
                    print("--------------------------------------------------")
                #Se genera un submenu que solicita al usuario si desea o no agregar otro producto
                #Llegado el caso se solicite otro prodcuto se repetira el proceso desde el punto donde se solicitan los datos del producto
                #Aqui se manejan los mismos controles contra errores
                #Si la elección es si se almacena un nuevo diccionario en el diccionario det_pedido[codped], lo cual generaria una lista de diccionarios
                while True:
                    try:
                        print("¿Desea agregar otro producto al pedido?")
                        print("1. SI\n2. NO")
                        opc=int(input("Digite su elección: "))
                        if opc==1:
                            print("--------------------------------------------------")
                            print("Ingrese la información del nuevo producto")
                            print("--------------------------------------------------")
                            break
                        elif opc==2:
                            print("--------------------------------------------------")
                            print("Pedido Registrado con Exito")
                            print("--------------------------------------------------")
                            return
                        else:
                            print("--------------------------------------------------")
                            print("Opciòn invalida, vuelva a digitar")
                            print("--------------------------------------------------")
                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")
                    
                break
            break

def visua_pedidos():
    #Se inicializa un for que recorre todos los pedidos existentes
    #Como una de las llaves corresponde a un diccionario con listas de diccionarios, se debe realizar un for adicional a lo normal
    #Cuando el llegue a "Detalles del pedido", entrara a un for que recorre dichas listas de diccionarios
    for i in pedidos:
        print("--------------------------------------------------")
        print("Pedido-->",i)
        print("--------------------------------------------------")
        for j in pedidos[i]:
            if j=="Detalles del pedido":
                print("--------------------------------------------------")
                print("Detalles del pedido")
                for x in pedidos[i][j]:
                    print("--------------------------------------------------")
                    for h in x:
                        print(h,"-",x[h])
            else:
                print(j,"-",pedidos[i][j])

def elimi_pedido():
    #Se solicita el codigo del pedido a eliminar, y se verifica que realmente exista
    while True:  
        while True:
            print("Digite el codigo del pedido que desea eliminar")
            codped=input("CPE-")
            if codped.isdigit(): 
                codped = f"CPE-{codped}"  
                break
            else:
                print("Ingrese solo numeros.")

        eva=pedidos.get(codped)
        if eva==None:
            print("Codigo de pedido inexistente, digite uno nuevo")
        else:
            break
    #Una vez se verifica el codigo, se le pregunta al usuario si realmente desea eliminar ese pedido
    while True:
        try:
            print("--------------------------------------------------")
            print("Esta seguro de eliminar el pedido: ",codped)
            print("1. SI\n2. NO")
            print("--------------------------------------------------")
            opc=int(input("Digite el numero de acuerdo a su elección: "))
            if opc==1:
                pedidos.pop(codped)
                print("Pedido Eliminado exitosamente")
                #Se eliminan los diccionarios bajo la llave del codigo, tanto en pedidos como en detalles, con .po
                det_pedido.pop(codped)
                break
            elif opc==2:
                break
            else:
                print("--------------------------------------------------")
                print("Opciòn invalida, vuelva a digitar")
        except ValueError:
            print("")
            print("Opciòn invalida (SOLO NUMEROS)")

def visua_inv():
    #Se usa una estructura for normal que va recorrer cada uno de los diccionarios incluidos en productos bajo el codigo del producto
    for i in productos:
        print("--------------------------------------------------")
        print("Codigo de Producto-->",i)
        print("--------------------------------------------------")
        for j in productos[i]:
            print(j,"-",productos[i][j])

def edit_ped():
    #Se solicita el codigo del pedido, se verifica su existencia, se limitan errores, etc
    while True:  
        while True:
            print("Digite el codigo del pedido que desea editar")
            codped=input("CPE-")
            if codped.isdigit(): 
                codped = f"CPE-{codped}"  
                break
            else:
                print("Ingrese solo numeros.")

        eva=pedidos.get(codped)
        if eva==None:
            print("Codigo de pedido inexistente, digite uno nuevo")
        else:
            break
    print("--------------------------------------------------")
    print("A continuación se visualiza la información del pedido")
    print("--------------------------------------------------")
    #Se imprime la información de dicho pedido, bajo la misma estructura de la funcion para visualizar pedidos
    for j in pedidos[codped]:
            if j=="Detalles del pedido":
                print("--------------------------------------------------")
                print("Detalles del pedido")
                for x in pedidos[codped][j]:
                    print("--------------------------------------------------")
                    for h in x:
                        print(h,"-",x[h])
            else:
                print(j,"-",pedidos[codped][j])
    #Se le pregunta al usuario la información que desea editar
    while True:
        try:
            print("--------------------------------------------------")
            print("1. Cambiar de producto\n2. Cambiar la cantidad\n3. Cancelar")
            print("--------------------------------------------------")
            opc=int(input("Digite de acuerdo a su elección: "))
            print("--------------------------------------------------")
            if opc==1:
                #Si se elige sustituir el producto, lo primero que veremos sera la lista de solicitudes que tiene ese pedido
                #En otras palabras se imprimen los productos con sus detalles en ese pedido
                #Par esto se una un for que recorre en el rango dado por el len() de lo alamcenado en "Detalles del pedido"
                #Esta averiguando la cantidad de listas de diccionarios, es decir averiguando cuando productos tiene
                #Para finalmente imprimirlos
                for count in range(len(pedidos[codped]["Detalles del pedido"])):
                    print("--------------------------------------------------")
                    print("SOLICITUD #",count+1)
                    print("--------------------------------------------------")
                    for i in pedidos[codped]["Detalles del pedido"][count]:
                        print(i, "-", pedidos[codped]["Detalles del pedido"][count][i])
                #Aqui
                while True:
                    try:
                        #Aqui se le solicita al usuario que ingrese el numero de solicitud que desea editar
                        print("--------------------------------------------------")
                        opc=int(input("Digite el numero de Solicitud que desea editar: "))
                        print("--------------------------------------------------")
                        
                        #aqui se verifica que la opción elegida si se encuentre en el rango de 1 a el largo del diccionario (Cant solicitudes)
                        if 1<=opc<=len(pedidos[codped]["Detalles del pedido"]):
                            #Una vez verificada la elección procedemos a eliminar la información de dicha solicitud
                            #Procedemos a restaurar el stock del producto que se va sustituir
                            #Eliminamos con la función del el diccionario ubicado en la posición opc-1, que corresponde a la solicitud que eligio el usuario
                            #Porque opc-1? sencillo porque las iteraciones empiezan a contar desde cero, si dejamos el valor que ingresa el usuario estariamos fuera de indice
                            #Recordemos que hablamos de una lsita de diccionarios
                            cant=pedidos[codped]["Detalles del pedido"][opc-1]["Cantidad"]
                            productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"])+cant
                            del pedidos[codped]["Detalles del pedido"][opc-1]

                            #Se da inicio a la solicitud de los datos del nuevo producto, tal cual como en la función agregar pedido
                            #Se sigue la misma logica que arriba
                            while True:
                                while True:
                                    while True:
                                        print("Digite el codigo del nuevo producto que solicita")
                                        codpro=input("CP-")
                                        if codpro.isdigit():  
                                            codpro = f"CP-{codpro}" 
                                            break
                                        else:
                                            print("Ingrese solo numeros")

                                    eva=productos.get(codpro)

                                    if eva==None:
                                        print("Codigo de producto inexistente, intente nuevamente")
                                        break
                                    else:  
                                        if productos[codpro]["Cantidad en Stock"] <= 0:
                                            print("Producto agotado, no se puede realizar el pedido")
                                            print("--------------------------------------------------")
                                            break
                                        else:
                                            while True:
                                                while True:
                                                    try:
                                                        cant=int(input("Digite la cantidad a solicitar: "))
                                                        if cant>0:
                                                            break
                                                        else:
                                                            print("--------------------------------------------------")
                                                            print("Valor Invalido, intente nuevamente")
                                                            print("--------------------------------------------------")

                                                    except ValueError:
                                                        print("--------------------------------------------------")
                                                        print("Opciòn invalida (SOLO NUMEROS)")
                                                        print("--------------------------------------------------")

                                                if ((productos[codpro]["Cantidad en Stock"])-cant)<0:
                                                    print("Imposible solicitar dicha cantidad, digite una nueva")
                                                else: 
                                                    productos[codpro]["Cantidad en Stock"]=productos[codpro]["Cantidad en Stock"]-cant
                                                    break
                                    
                                    detalles={"Codigo de pedido":codped,"Codigo de producto":codpro,"Cantidad":cant,"Precio Unidad":productos[codpro]["Precio de venta"],"Numero de Linea":1}
                                    det_pedido[codped].append(detalles)
                                    pedidos[codped]["Detalles del pedido"]=det_pedido[codped]
                                    if productos[codpro]["Cantidad en Stock"]<5:
                                        print("--------------------------------------------------")
                                        print("ALERTA: SOLO RESTAN ", productos[codpro]["Cantidad en Stock"] ," UNIDADES DE",productos[codpro]["Nombre"])
                                        print("--------------------------------------------------")
                                        print("Ediciòn Exitosa")
                                        print("--------------------------------------------------")
                                        break
                                    else:
                                        print("--------------------------------------------------")
                                        print("Ediciòn Exitosa")
                                        print("--------------------------------------------------")
                                        break
                                break
                            break
                        else:
                            print("Opción no valida, vuelva a intentar")
                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")
                break

            elif opc==2:
                #Igual que la opc 1, mostramos las solicitudes o los detalles de los prodcutos solicitados en ese pedido
                for count in range(len(pedidos[codped]["Detalles del pedido"])):
                    print("--------------------------------------------------")
                    print("SOLICITUD #",count+1)
                    print("--------------------------------------------------")
                    for i in pedidos[codped]["Detalles del pedido"][count]:
                        print(i, "-", pedidos[codped]["Detalles del pedido"][count][i])

                while True:
                    try:
                        print("--------------------------------------------------")
                        opc=int(input("Digite el numero de Solicitud que desea editar: "))
                        print("--------------------------------------------------")
                        #Tal cual como arriba verificamos la eleccion con un if usando len y restaurando la cantidad del stock
                        if 1<=opc<=len(pedidos[codped]["Detalles del pedido"]):
                            
                            cant=pedidos[codped]["Detalles del pedido"][opc-1]["Cantidad"]
                            productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"])+cant
                            #Exactamente el mismo proceso que en la parte donde se solicita la cantidad del producto en agregar pedidos
                            while True:
                                while True:
                                    try:
                                        cant=int(input("Digite la cantidad a solicitar: "))
                                        if cant>0:
                                            break
                                        else:
                                            print("--------------------------------------------------")
                                            print("Valor Invalido, intente nuevamente")
                                            print("--------------------------------------------------")

                                    except ValueError:
                                        print("--------------------------------------------------")
                                        print("Opciòn invalida (SOLO NUMEROS)")
                                        print("--------------------------------------------------")

                                if ((productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"])-cant)<0:
                                    print("Imposible solicitar dicha cantidad, digite una nueva")
                                else: 
                                    productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"])-cant
                                    break
                                
                            pedidos[codped]["Detalles del pedido"][opc-1]["Cantidad"]=cant
                            
                            if productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"]<5:
                                    print("--------------------------------------------------")
                                    print("ALERTA: SOLO RESTAN ", productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"] ," UNIDADES DE",productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Nombre"])
                                    print("--------------------------------------------------")
                                    print("Ediciòn Exitosa")
                                    print("--------------------------------------------------")
                                    break
                            else:
                                print("--------------------------------------------------")
                                print("Ediciòn Exitosa")
                                print("--------------------------------------------------")
                                break
                        else:
                            print("--------------------------------------------------")
                            print("Opciòn invalida")
                            print("--------------------------------------------------")

                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")
                break

            elif opc==3:
                break
            else:
                print("--------------------------------------------------")
                print("Opciòn invalida")
                print("--------------------------------------------------")

        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS)")
            print("--------------------------------------------------")

def buscar():
    #Se solicita el metodo de busqueda, se usan las mismas validaciones que se usaron anteriormente, para evitar errores
    while True:
        try:
            print("--------------------------------------------------")
            print("1. Buscar por Nombre\n2. Buscar por Categoria\n3. Buscar por Codigo\n4. Salir")
            print("--------------------------------------------------")
            opc=int(input("Digite la opciòn deseada: "))
            print("--------------------------------------------------")

            if opc==1:
                #Se solicita al usuario que ingrese el nombre del producto
                #Y se recorre productos para verificar su existencia, una vez encontrado se imprime la información del mismo
                #Usamos la variable noti para corroborar que se encuentre algun producto, caso contrario avisa al usaurio de la inexistencia del mismo
                nom=input("Digite el nombre del producto: ")
                noti=0
                for i in productos:
                    
                    if productos[i]["Nombre"]==nom:
                        noti=2
                        print("--------------------------------------------------")
                        print("Codigo de Producto-->",i)
                        print("--------------------------------------------------")
                        for j in productos[i]:
                            print(j,"-",productos[i][j])

                if noti!=2:
                    print("--------------------------------------------------")
                    print("Producto No existe")
                    print("--------------------------------------------------")

            elif opc==2:
                #Se solicita la categoria por la cual desea buscar o filtrar los productos
                #Se usan las mismas validaciones
                noti=0
                while True:
                    try:
                        print("--------------------------------------------------")
                        print("1. Pan\n2. Pastel\n3. Postre ")
                        print("--------------------------------------------------")
                        opc=int(input("Seleccione la categoria del producto: "))
                        
                        if opc==1:
                            nom="Pan"
                            break
                        elif opc==2:
                            nom="Pastel"
                            break
                        elif opc==3:
                            nom="Postre"
                            break
                        else:
                            print("--------------------------------------------------")
                            print("Opciòn invalida, vuelva a digitar")
                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")
                #Se recorre el diccionario productos para imprimir la información de los productos bajo la categoria elegida
                #Igualmente se usa noti para verificar que se encontro al menos uno
                for i in productos:
                        
                    if productos[i]["Categoria"]==nom:
                        noti=2
                        print("--------------------------------------------------")
                        print("Codigo de Producto-->",i)
                        print("--------------------------------------------------")
                        for j in productos[i]:
                            print(j,"-",productos[i][j])

                if noti!=2:
                    print("--------------------------------------------------")
                    print("No hay productos de esta categoria")
                    print("--------------------------------------------------")


            elif opc==3:
                #Se solicita el codigo del producto y se verifica que exista en el diccionario productos
                #Una vez encontrado se imprime la información de dicho producto
                while True:
                    print("Digite el codigo del producto")
                    nom=input("CP-")
                    if nom.isdigit():  
                        nom = f"CP-{nom}" 
                        break
                    else:
                        print("Ingrese solo numeros.")
                
                eva=productos.get(nom,1)
                
                if eva==1:
                    print("Producto no existe")
                else:
                    print("--------------------------------------------------")
                    print("Codigo de Producto-->",nom)
                    print("--------------------------------------------------")
                    for i in productos[nom]:
                        print(i,"-",productos[nom][i])

            elif opc==4:
                break
            else:
                print("--------------------------------------------------")
                print("Opción invalida vuelva a intentar")
                print("--------------------------------------------------")
        
        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS)")
            print("--------------------------------------------------")

def buscar_pedidos():
    #Se solicita el metodo de busqueda
    while True:
        try:
            print("--------------------------------------------------")
            print("1. Buscar por Codigo\n2. Filtrar pedidos por producto\n3. Salir")
            print("--------------------------------------------------")
            opc=int(input("Digite la opciòn deseada: "))
            print("--------------------------------------------------")

            if opc==1:
                #Se solicita el codigo del pedido, se verifica que exista y se imprime su información
                while True:
                    print("Digite el codigo del pedido")
                    nom=input("CPE-")
                    if nom.isdigit():  
                        nom = f"CPE-{nom}" 
                        break
                    else:
                        print("Ingrese solo numeros")
                
                eva=pedidos.get(nom,1)
                
                if eva==1:
                    print("--------------------------------------------------")
                    print("Pedido no existe")
                    print("--------------------------------------------------")
                else:
                    print("--------------------------------------------------")
                    print("Codigo de Pedido-->",nom)
                    print("--------------------------------------------------")
                    for j in pedidos[nom]:
                        if j=="Detalles del pedido":
                            print("--------------------------------------------------")
                            print("Detalles del pedido")
                            for x in pedidos[nom][j]:
                                print("--------------------------------------------------")
                                for h in x:
                                    print(h,"-",x[h])
                        else:
                            print(j,"-",pedidos[nom][j])

            elif opc==2:
                #Se abre el submenu, ya que se puede filtrar por nombre o codigo de producto inmerso en los pedidos
                noti=0
                while True:
                    try:
                        print("--------------------------------------------------")
                        print("1. Nombre de Producto\n2. Codigo de producto\n3. Cancelar")
                        print("--------------------------------------------------")
                        opc=int(input("Digite su elección: "))
                        #Primero se verifica la existencia del producto en el diccionario productos
                        #Se valida con noti=2
                        if opc==1:
                            noti=0
                            while True:
                                try:
                                    nom=input("Digite el nombre del producto: ")
                                    for i in productos:
                                        if productos[i]["Nombre"]==nom:
                                            noti=2
                                            cod=i

                                    if noti==2:
                                        print("Producto validado")
                                        break
                                    else:
                                        print("--------------------------------------------------")
                                        print("Producto No existe, ingrese uno nuevo")
                                        print("--------------------------------------------------")    

                                except ValueError:
                                    print("--------------------------------------------------")
                                    print("Opciòn invalida")
                                    print("--------------------------------------------------")

                            #Una vez validado se ingresa en un ciclo de distintos for, tanto para su busqueda como impresión de información
                            #FUE UN DOLOR DE CABEZA ESTO PROFE
                            #Primero recorro pedidos, luego recorro las llaves de pedido en la posición recorrida
                            #Cuando llegue a detalles del pedido que es lo que requerimos
                            #Empieza a recorrer esa llave, es decir la listas de diccionarios incluidas en la llave, que corresponde a los detalles
                            #Luego recorremos los detalles del pedido, si hay mas de un producto ingresado hay que recorrer mas de un diccionario
                            #Cuando llegue a la llave codigo de producto, verifica si corresponde o no al codigo ingresado por el usuario
                            #De ser igual imprime la información del pedido
                            #IMPORTANTE, ESTAMOS BUSCANDO POR NOMBRE, PERO ANTERIORMENTE EXTRAIMOS EL CODIGO DEL PRODUCTO MEDIANTE SU NOMBRE, PARA HACER MAS SENCILLA LA BUSQUEDA
                            for i in pedidos:
                                for j in pedidos[i]:
                                    if j=="Detalles del pedido":
                                        for x in pedidos[i][j]:
                                            for h in x:
                                                if h=="Codigo de producto":
                                                    if x[h]==cod:
                                                        codped=i
                                                        noti=2
                                                        print("--------------------------------------------------")
                                                        print("Pedido-->",codped)
                                                        print("--------------------------------------------------")
                                                        for e in pedidos[codped]:
                                                            if e=="Detalles del pedido":
                                                                print("--------------------------------------------------")
                                                                print("Detalles del pedido")
                                                                for p in pedidos[codped][e]:
                                                                    print("--------------------------------------------------")
                                                                    for o in p:
                                                                        print(o,"-",p[o])
                                                            else:
                                                                print(e,"-",pedidos[codped][e])
                                                            

                            if noti!=2:
                                print("--------------------------------------------------")
                                print("No hay pedidos con dicho producto incluido")
                                print("--------------------------------------------------") 
                                break

                        elif opc==2:
                            noti=0
                            #Hacemos exactamente el mismo proceso que en la opc 1, la unica diferencia es que ahora no debemos buscar el codigo del producto
                            while True:
                                try:  
                                    while True:
                                        print("Digite el codigo del producto")
                                        cod=input("CP-")
                                        if cod.isdigit():  
                                            cod = f"CP-{cod}" 
                                            break
                                        else:
                                            print("--------------------------------------------------")
                                            print("Ingrese solo numeros")
                                            print("--------------------------------------------------")
                                    
                                    eva=productos.get(cod,1)
                                    if eva==1:
                                        print("Codigo de producto inexistente, ingrese uno nuevo")
                                    else:
                                        break

                                except ValueError:
                                    print("--------------------------------------------------")
                                    print("Opciòn invalida (SOLO NUMEROS)")
                                    print("--------------------------------------------------")

                            for i in pedidos:
                                for j in pedidos[i]:
                                    if j=="Detalles del pedido":
                                        for x in pedidos[i][j]:
                                            for h in x:
                                                if h=="Codigo de producto":
                                                    if x[h]==cod:
                                                        codped=i
                                                        noti=2
                                                        print("--------------------------------------------------")
                                                        print("Pedido-->",codped)
                                                        print("--------------------------------------------------")
                                                        for e in pedidos[codped]:
                                                            if e=="Detalles del pedido":
                                                                print("--------------------------------------------------")
                                                                print("Detalles del pedido")
                                                                for p in pedidos[codped][e]:
                                                                    print("--------------------------------------------------")
                                                                    for o in p:
                                                                        print(o,"-",p[o])
                                                            else:
                                                                print(e,"-",pedidos[codped][e])
                                                            
                            if noti!=2:
                                print("--------------------------------------------------")
                                print("No hay pedidos con dicho codigo de producto")
                                print("--------------------------------------------------") 
                                break

                        elif opc==3:
                            break
                        else:
                            print("--------------------------------------------------")
                            print("Opciòn invalida")
                            print("--------------------------------------------------")
                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")

            elif opc==3:
                break
            else:
                print("--------------------------------------------------")
                print("Opción invalida vuelva a intentar")
                print("--------------------------------------------------")
        
        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS)")
            print("--------------------------------------------------")