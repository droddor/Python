def generador(n):
    while n >=0:
        yield n
        n -= 1

# x= generador(3)

for valor in generador(3):
    print(valor)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))