from optparse import make_option


def cuadrado(numero):
    return numero ** 2

l = [1,2,3]
l2 = list(map(cuadrado, l)) # esto crea un objeto de tipo lista pero no es la lista. Hay que hacer un casting

l3 = map(cuadrado, l)

print(l3)

for i in l2:
    print(i)

print(l2)