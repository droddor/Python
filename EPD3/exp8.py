# Funcion lambda que recibe dos paramentros x = lambda a,b
# : devuelve una tupla (b+1, a+1) y la devuelve en el orden que tu se la des

x = lambda a, b: (b+1, a+1)
print(x(3, 9))

x = lambda c, d: (c*10, d*20)

print(x(2,2))

# Nombre app = lambda arg1, arg2 : que devuelve
aplicarDto = lambda fPrecio, fDescuento: fPrecio - (fPrecio * fDescuento /100)

print(f"Precio con descuento aplicado: {aplicarDto(100,20)}")
print(f"Precio con descuento aplicado: {aplicarDto(200,20)}")