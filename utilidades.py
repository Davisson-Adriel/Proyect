productos={'PH': {'Nombre': 'CDC', 'Categoria': 'Pastel', 'Descripcion': 'EDEWQ', 'Proovedor': 'EWEWEW', 'Cantidad en Stock': 30, 'Precio de venta': 3.0, 'Precio de Proovedor': 4.0}}
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
    print("1. Registrar nuevo pedido\n2. Visualizar Pedidos\n3. Editar Pedido\n4. Eliminar pedido\n5. Salir")
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
            print("Ingrese solo numeros.")
    
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
        print(productos)
    else:
        print("--------------------------------------------------")
        print("Codigo de producto ya existente")
        print("--------------------------------------------------")

def ag_pedido():
    
    print("--------------------------------------------------")
    print("Registro de nuevo pedido")
    print("--------------------------------------------------")
    
    while True:
        print("Digite el codigo del cliente")
        codcliente=input("CC-")
        if codcliente.isdigit():  
            codcliente = f"CC-{codcliente}"  
            break
        else:
            print("Ingrese solo numeros.")
    
    while True:  
        while True:
            print("Digite el codigo del pedido")
            codped=input("CPE-")
            if codped.isdigit(): 
                codped = f"CPE-{codped}"  
                break
            else:
                print("Ingrese solo numeros.")

        eva=pedidos.get(codped)
        if eva!=None:
            print("Codigo de pedido existente, digite uno nuevo")
        else:
            break

    dia=int(input("Digite el dia (numerico): "))
    dia=str(dia)
    mes=int(input("Digite el mes (numerico): "))
    mes=str(mes)
    año=int(input("Digite el año: "))
    año=str(año)
    fecha=str(año+"/"+mes+"/"+dia)
    
    while True:
        while True:
            codpro=input("Digite el codigo del producto a solicitar: ")
            eva=productos.get(codpro,1)
            if eva==1:
                print("Codigo de producto inexistente, intente nuevamente")
                
            else:
                
                if productos[codpro]["Cantidad en Stock"] <= 0:
                    print("Producto agotado, no se puede realizar el pedido")
                    print("--------------------------------------------------")
                    break
                else:
                    while True:
                        cant=int(input("Digite la cantidad a solicitar: "))
                        if ((productos[codpro]["Cantidad en Stock"])-cant)<0:
                            print("Imposible solicitar dicha cantidad, digite una nueva")
                        else: 
                            productos[codpro]["Cantidad en Stock"]=productos[codpro]["Cantidad en Stock"]-cant
                            break
                break
        
        
        detalles={"Codigo de pedido":codped,"Codigo de producto":codpro,"Cantidad":cant,"Precio Unidad":productos[codpro]["Precio de venta"],"Numero de Linea":1}
        det_pedido[codped]=detalles
        ped={"Codigo de pedido":detalles["Codigo de pedido"],"Codigo de cliente":codcliente,"Fecha":fecha,"Detalles del pedido":det_pedido[codped]}
        pedidos[ped["Codigo de pedido"]]=ped
        if productos[codpro]["Cantidad en Stock"]<5:
            print("--------------------------------------------------")
            print("ALERTA: SOLO RESTAN ", productos[codpro]["Cantidad en Stock"] ," UNIDADES DE",productos[codpro]["Nombre"])
            print("--------------------------------------------------")
        print("Pedido Registrado con Exito")
        print("--------------------------------------------------")
        break

def visua_pedidos():
    
    for i in pedidos:
        print("--------------------------------------------------")
        print("Pedido-->",i)
        print("--------------------------------------------------")
        for j in pedidos[i]:
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
            print(j,"-",pedidos[codped][j])

    while True:
        try:
            print("--------------------------------------------------")
            print("1. Cambiar de producto\n2. Cambiar la cantidad\n3. Cancelar")
            print("--------------------------------------------------")
            opc=int(input("Digite de acuerdo a su elección: "))
            print("--------------------------------------------------")
            if opc==1:
                
                while True:
                    
                    while True:
                        print("Digite el codigo del nuevo producto")
                        codpro2=input("CP-")
                        if codpro2.isdigit():  
                            codpro2 = f"CP-{codpro2}" 
                            break
                        else:
                            print("Ingrese solo numeros.")

                    eva=productos.get(codpro2,1)
                    if eva==1:
                        print("Codigo de producto inexistente, intente nuevamente")
                    else:
                        
                        if productos[codpro2]["Cantidad en Stock"] <= 0:
                            print("Producto agotado, no se puede hacer la edición")
                            print("--------------------------------------------------")
                            break
                        else:
                            while True:
                                cant=int(input("Digite la cantidad a solicitar: "))
                                if ((productos[codpro2]["Cantidad en Stock"])-cant)<0:
                                    print("Imposible solicitar dicha cantidad, digite una nueva")
                                else: 
                                    productos[codpro2]["Cantidad en Stock"]=(productos[codpro2]["Cantidad en Stock"])-cant
                                    break
                        break
                

                cant2=pedidos[codped]["Detalles del pedido"]["Cantidad"]
                productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"])+cant2
                pedidos[codped]["Detalles del pedido"]["Codigo de producto"]=codpro2
                pedidos[codped]["Detalles del pedido"]["Cantidad"]=cant
                pedidos[codped]["Detalles del pedido"]["Precio Unidad"]=productos[codpro2]["Precio de venta"]
                
                print("--------------------------------------------------")
                print("Edición realizada con exito")
                print("--------------------------------------------------")
                break

            elif opc==2:
                
                cant2=pedidos[codped]["Detalles del pedido"]["Cantidad"]
                productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"])+cant2

                while True:
                    cant=int(input("Digite la nueva cantidad a solicitar: "))
                    if ((productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"])-cant)<0:
                        print("Imposible solicitar dicha cantidad, digite una nueva")
                    else: 
                        productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"]=(productos[pedidos[codped]["Detalles del pedido"]["Codigo de producto"]]["Cantidad en Stock"])-cant
                        break
                
                pedidos[codped]["Detalles del pedido"]["Cantidad"]=cant
                print("--------------------------------------------------")
                print("Edición realizada con exito")
                print("--------------------------------------------------")
                break

            elif opc==3:
                break
            else:
                print("")
                print("Opciòn invalida, intente nuevamente")

        except ValueError:
            print("")
            print("Opciòn invalida (SOLO NUMEROS)")

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
            print("")
            print("Opciòn invalida (SOLO NUMEROS)")