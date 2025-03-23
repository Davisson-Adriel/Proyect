import json
from utilidades import pedidos,det_pedido,productos
#Guardamos los archivos json bajo variables para hacer mas sencillo su proceso
pedidos_json="pedidos.json"
det_pedido_json="detalle.json"
productos_json="productos.json"

def guardar_datos():
    #Esta función me almacena y actualiza la información de los diccionarios pedidos, det_pedido y productos
    #Aqui abrimos el archivo alamcenado dentro de pedidos_json en modo W osea escritura para ingresar información
    #Posteriormente el .dump nos permite ingresar lo que se encuentra en pedidos, dentro de archivo con una sangria 4 para mas legibilidad

    with open(pedidos_json,"w") as archivo:
        json.dump(pedidos, archivo, indent=4)

    with open(det_pedido_json,"w") as archivo1:
        json.dump(det_pedido, archivo1, indent=4)

    with open(productos_json,"w") as archivo2:
        json.dump(productos, archivo2, indent=4)


def cargar_datos(archivo):
    #Creamos datos para guardar la información del archivo json que vamos a leer
    #Abrimos el arcivo (Arguento), que corresponde al nombre del archivo json
    #Le cambiamos el nombre a file para mayor comodidad
    #Cargamos los datos de ese archivo con .load en el diccionario datos
    #Luego asignamos condicionales para indicarle al sistema en que diccionario vamos a almacenar la información dependiendo del nombre de documento ingresado
    #Usamos .uptade para que no se sobrescriban datos, si no que solo cree la información partiendo de lo qeu se ecuentra en los archivos json
    datos = {}
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
    except Exception:
        print("")
        datos = None
    if archivo == "productos.json":
        productos.update(datos)
    elif archivo == "pedidos.json":
        pedidos.update(datos)
    elif archivo == "detalle.json":
        det_pedido.update(datos)