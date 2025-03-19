from utilidades import*
print("--------------------------------------------------")
print("Bienvenido a Digital Delicias Casera")

while True:

    mostrar_menu()
    opc=pedir_opc()

    if opc==1:
        ag_producto()
    elif opc==2:
        while True:
            menu_pedidos()
            opc=pedir_opc()
            if opc==1:
                ag_pedido()
            elif opc==2:
                visua_pedidos()
            elif opc==3:
                print("Editar Pedido")
            elif opc==4:
                elimi_pedido()
            elif opc==5:
                break
            else:
                print("")
                print("Opciòn invalida, intente nuevamente")
    elif opc==3:
        print("")
    elif opc==4:
        print("")
        print("Hasta luego querido usuario")
        break
    else:
        print("")
        print("Opciòn invalida, intente nuevamente")

