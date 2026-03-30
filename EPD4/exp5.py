import json

lista_productos = []

print("Introduzca productos al inventario (escriba FIN en el nombre para terminar)")

sNombre = input("Introduzca el nombre del producto: ")
while sNombre != "FIN":
    try:
        fPrecio = float(input(f"Introduzca el precio del producto {sNombre}: "))
        producto = {"item": sNombre, "precio": fPrecio}
        lista_productos.append(producto)
    except ValueError:
        print("Introduzca un precio valido")

    sNombre = input("Introduzca el nombre del producto: ")
try:
    with open("productos.json", "w") as outfile:
        json.dump(lista_productos, outfile)
    print(f"Productos {len(lista_productos)} actualizados como JSON")
except IOError as e:
    print(f"Error al crear el archivo {e}")


