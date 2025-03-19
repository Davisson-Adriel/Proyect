productos={'PH': {'Nombre': 'CDC', 'Categoria': 'Pastel', 'Descripcion': 'EDEWQ', 'Proovedor': 'EWEWEW', 'Cantidad en Stock': 30, 'Precio de venta': 3.0, 'Precio de Proovedor': 4.0}}
pedidos={}
det_pedido={}

def mostrar_menu():
    print("--------------------------------------------------")
    print(" ")
    print("1. Registro de productos\n2. Pedidos\n3. Consultas\n4. Salir")
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
        nom=input("Nombre del Producto: ")
        while True:
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
        
        des=input("Descripción del producto: ")
        pro=input("Proovedor: ")
        cantstock=int(input("Cantidad en Stock: "))
        preventa=float(input("Precio de Venta: "))
        prepro=float(input("Precio de Proovedor: "))
        codigo={"Nombre":nom,"Categoria":cat,"Descripcion":des,"Proovedor":pro,"Cantidad en Stock":cantstock,"Precio de venta":preventa,"Precio de Proovedor":prepro}
        productos[cod]=codigo
        print("--------------------------------------------------")
        print("PRODUCTO AGREGADO CON EXITO")
        print("--------------------------------------------------")
        print(productos)
    else:
        print("--------------------------------------------------")
        print("Codigo de producto ya existente")

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