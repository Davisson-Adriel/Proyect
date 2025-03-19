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
    print("1. Registrar nuevo pedido\n2. Visualizar Pedidos\n3. Editar Pedido\n4. Salir")
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
    cod=input("Codigo del producto: ")
    eva=productos.get(cod,1)
    if eva==1:
        nom=input("Nombre del Producto: ")
        while True:
            print("--------------------------------------------------")
            print("1. Pan\n2. Pastel\n3. Postre ")
            print("--------------------------------------------------")
            opc=int(input("Seleccione la categoria del producto"))
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
    else:
        print("--------------------------------------------------")
        print("Codigo de producto ya existente")

def ag_pedido():
    
    print("--------------------------------------------------")
    print("Registro de nuevo pedido")
    print("--------------------------------------------------")
    codcliente=input("Digite el codigo del cliente: ")
    dia=int(input("Digite el dia (numerico): "))
    dia=str(dia)
    mes=int(input("Digite el mes (numerico): "))
    mes=str(mes)
    año=int(input("Digite el año: "))
    año=str(año)
    fecha=str(año+"/"+mes+"/"+dia)
    
    while True:
        codped=input("Digite el codigo del pedido: ")
        eva=pedidos.get(codped)
        if eva!=None:
            print("Codigo de pedido existente, digite uno nuevo")
        else:
            break

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
        det_pedido[detalles["Codigo de pedido"]]=detalles
        ped={"Codigo de pedido":detalles["Codigo de pedido"],"Codigo de cliente":codcliente,"Fecha":fecha,"Detalles del pedido":det_pedido}
        pedidos[ped["Codigo de pedido"]]=ped
        if productos[codpro]["Cantidad en Stock"]<5:
            print("--------------------------------------------------")
            print("ALERTA: SOLO RESTAN 5 UNIDADES DE",productos[codpro]["Nombre"])
            print("--------------------------------------------------")
        print("Pedido Registrado con Exito")
        print(pedidos)
        break
