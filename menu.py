from utilidades import*
print("--------------------------------------------------")
print("Bienvenido a Digital Delicias Casera")

while True:

    mostrar_menu()
    opc=pedir_opc()

    if opc==1:
        ag_producto()
    elif opc==2:
        print("")
    elif opc==3:
        print("")
    elif opc==4:
        print("")
        print("Hasta luego querido usuario")
        break
    else:
        print("")
        print("Opciòn invalida, intente nuevamente")

