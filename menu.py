from utilidades import*
print("--------------------------------------------------")
print("Bienvenido a Digital Delicias Casera")

while True:
    try:
        mostrar_menu()
        opc=pedir_opc()

        if opc==1:
            ag_producto()
            
        elif opc==2:
            while True:
                try:
                    menu_pedidos()
                    opc=pedir_opc()
                    if opc==1:
                        ag_pedido()
                    elif opc==2:
                        visua_pedidos()
                    elif opc==3:
                        buscar_pedidos()
                    elif opc==4:
                        edit_ped()
                    elif opc==5:
                        elimi_pedido()
                    elif opc==6:
                        break
                    else:
                        print("")
                        print("Opciòn invalida, intente nuevamente")
                except ValueError:
                    print("")
                    print("Opciòn invalida (SOLO NUMEROS)")

        elif opc==3:
            while True:
                try:
                    menu_consultas()
                    opc=pedir_opc()
                    if opc==1:
                        buscar()
                    elif opc==2:
                        visua_inv()
                    elif opc==3:
                        break
                    else:
                        print("")
                        print("Opciòn invalida, intente nuevamente")
                except ValueError:
                    print("")
                    print("Opciòn invalida (SOLO NUMEROS)")

        elif opc==4:
            print("")
            print("Hasta luego querido usuario")
            print()
            break
        else:
            print("")
            print("Opciòn invalida, intente nuevamente")

    except ValueError:
        print("")
        print("Opciòn invalida (SOLO NUMEROS)")
