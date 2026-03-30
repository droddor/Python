def generador():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


for i in generador():
    print("Yield",i)