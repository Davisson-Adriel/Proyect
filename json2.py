import json
from utilidades import pedidos,det_pedido,productos

pedidos_json="pedidos.json"
det_pedido_json="detalle.json"
productos_json="productos.json"

def guardar_datos():
    with open(pedidos_json,"w") as archivo:
        json.dump(pedidos, archivo, indent=4)

    with open(det_pedido_json,"w") as archivo1:
        json.dump(det_pedido, archivo1, indent=4)

    with open(productos_json,"w") as archivo2:
        json.dump(productos, archivo2, indent=4)

