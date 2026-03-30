l = [1,2,3]
l2 = (n ** 2 for n in l)
print(l2)

# l2 es un generador no una lista
# una vez entregado el resultado se queda vacio.
print(list(l2))
print(list(l2))