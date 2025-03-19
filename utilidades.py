productos={'PH': {'Nombre': 'CDC', 'Categoria': 'Pastel', 'Descripcion': 'EDEWQ', 'Proovedor': 'EWEWEW', 'Cantidad en Stock': 30, 'Precio de venta': 3.0, 'Precio de Proovedor': 4.0}}


def mostrar_menu():
    print("--------------------------------------------------")
    print(" ")
    print("1. Registro de productos\n2. Pedidos\n3. Consultas")
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


