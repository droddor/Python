import random

def sucesos(probabilidad):
    while True:
        yield random.random() < probabilidad




probabilidad = 0.3 # Entre [0,1] le damos 30%
contador = 0

for evento in sucesos(probabilidad):
    print(evento)
    contador += 1
    if contador > 5:
        break

