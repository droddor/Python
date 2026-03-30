def generador():
    yield 5

a = generador()
print(next(a))
#print(next(a))