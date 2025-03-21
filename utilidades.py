productos={'CP-001': {'Nombre': 'CDC', 'Categoria': 'Pastel', 'Descripcion': 'EDEWQ', 'Proovedor': 'EWEWEW', 'Cantidad en Stock': 30, 'Precio de venta': 3.0, 'Precio de Proovedor': 4.0}}
pedidos={}
det_pedido={}

def mostrar_menu():
    print("--------------------------------------------------")
    print(" ")
    print("1. Registro de productos\n2. Pedidos\n3. Consultas\n4. Salir")
    print(" ")
    print("--------------------------------------------------")

def menu_consultas():
    print("--------------------------------------------------")
    print(" ")
    print("1. Buscar Productos\n2. Mirar Inventario\n3. Salir")
    print(" ")
    print("--------------------------------------------------")

def menu_pedidos():
    print("--------------------------------------------------")
    print(" ")
    print("1. Registrar nuevo pedido\n2. Visualizar Pedidos\n3. Buscar Pedido\n4. Editar Pedido\n5. Eliminar pedido\n6. Salir")
    print(" ")
    print("--------------------------------------------------")

def pedir_opc():
    print("")
    opc=int(input("Digite la opciòn deseada: "))
    return opc

def ag_producto():
    print("--------------------------------------------------")
    print("Registro de nuevo producto")
    print("--------------------------------------------------")
    

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
        
        while True:
            nom=input("Nombre del Producto: ")
            if len(nom)>0:
                break
            else:
                print("No se puede dejar el nombre vacio")
        
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

        while True:
            des=input("Descripción del producto: ")
            if len(des)>0:
                break
            else:
                print("No se puede dejar la descripción vacia")

        while True:
            pro=input("Proovedor: ")
            if len(pro)>0:
                break
            else:
                print("No se puede dejar el proovedor vacio")
        
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

        codigo={"Nombre":nom,"Categoria":cat,"Descripcion":des,"Proovedor":pro,"Cantidad en Stock":cantstock,"Precio de venta":preventa,"Precio de Proovedor":prepro}
        productos[cod]=codigo
        print("--------------------------------------------------")
        print("PRODUCTO AGREGADO CON EXITO")
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("Codigo de producto ya existente")
        print("--------------------------------------------------")

def ag_pedido():
    
    print("--------------------------------------------------")
    print("Registro de nuevo pedido")
    print("--------------------------------------------------")
    
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

        eva=pedidos.get(codped)
        if eva!=None:
            print("Codigo de pedido existente, digite uno nuevo")
        else:
            break

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
    
    fecha=str(año+"/"+mes+"/"+dia)
    det_pedido[codped]=[]

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
                pedidos[codped]={"Codigo de pedido":codped,"Codigo de Cliente":codcliente,"Fecha":fecha,"Detalles del pedido":det_pedido[codped]}
                if productos[codpro]["Cantidad en Stock"]<5:
                    print("--------------------------------------------------")
                    print("ALERTA: SOLO RESTAN ", productos[codpro]["Cantidad en Stock"] ," UNIDADES DE",productos[codpro]["Nombre"])
                    print("--------------------------------------------------")

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
            break

def visua_pedidos():
    
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
    
    for i in productos:
        print("--------------------------------------------------")
        print("Codigo de Producto-->",i)
        print("--------------------------------------------------")
        for j in productos[i]:
            print(j,"-",productos[i][j])

def edit_ped():
    
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
    
    while True:
        try:
            print("--------------------------------------------------")
            print("1. Cambiar de producto\n2. Cambiar la cantidad\n3. Cancelar")
            print("--------------------------------------------------")
            opc=int(input("Digite de acuerdo a su elección: "))
            print("--------------------------------------------------")
            if opc==1:
                for count in range(len(pedidos[codped]["Detalles del pedido"])):
                    print("--------------------------------------------------")
                    print("SOLICITUD #",count+1)
                    print("--------------------------------------------------")
                    for i in pedidos[codped]["Detalles del pedido"][count]:
                        print(i, "-", pedidos[codped]["Detalles del pedido"][count][i])

                while True:
                    try:
                        print("--------------------------------------------------")
                        opc=int(input("Digite el numero de Solicitud que desea editar"))
                        print("--------------------------------------------------")
                        
                        if 1<=opc<=len(pedidos[codped]["Detalles del pedido"]):
                            
                            cant=pedidos[codped]["Detalles del pedido"][opc-1]["Cantidad"]
                            productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"])+cant
                            del pedidos[codped]["Detalles del pedido"][opc-1]


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
                        break
                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")
                break

            elif opc==2:
                for count in range(len(pedidos[codped]["Detalles del pedido"])):
                    print("--------------------------------------------------")
                    print("SOLICITUD #",count+1)
                    print("--------------------------------------------------")
                    for i in pedidos[codped]["Detalles del pedido"][count]:
                        print(i, "-", pedidos[codped]["Detalles del pedido"][count][i])

                while True:
                    try:
                        print("--------------------------------------------------")
                        opc=int(input("Digite el numero de Solicitud que desea editar"))
                        print("--------------------------------------------------")
                        
                        if 1<=opc<=len(pedidos[codped]["Detalles del pedido"]):
                            
                            cant=pedidos[codped]["Detalles del pedido"][opc-1]["Cantidad"]
                            productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"][opc-1]["Codigo de producto"]]["Cantidad en Stock"])+cant

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
                            
                    except ValueError:
                        print("--------------------------------------------------")
                        print("Opciòn invalida (SOLO NUMEROS)")
                        print("--------------------------------------------------")
                break

        except ValueError:
            print("--------------------------------------------------")
            print("Opciòn invalida (SOLO NUMEROS)")
            print("--------------------------------------------------")

def buscar():

    while True:
        try:
            print("--------------------------------------------------")
            print("1. Buscar por Nombre\n2. Buscar por Categoria\n3. Buscar por Codigo\n4. Salir")
            print("--------------------------------------------------")
            opc=int(input("Digite la opciòn deseada: "))
            print("--------------------------------------------------")

            if opc==1:
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

    while True:
        try:
            print("--------------------------------------------------")
            print("1. Buscar por Codigo\n2. Filtrar pedidos por producto\n3. Salir")
            print("--------------------------------------------------")
            opc=int(input("Digite la opciòn deseada: "))
            print("--------------------------------------------------")

            if opc==1:
                
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
                
                noti=0
                while True:
                    try:
                        print("--------------------------------------------------")
                        print("1. Nombre de Producto\n2. Codigo de producto\n3. Cancelar")
                        print("--------------------------------------------------")
                        opc=int(input("Digite su elección: "))
                        
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
                            print()




                        elif opc==3:
                            break
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