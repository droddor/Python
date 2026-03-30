import random

lPersonas = ["Daniel","Jose","Cleison","Adrian","Mario","David","Esteban","Antonio","Alvaro"]

def sortear(lPersonas):
    while True:
        yield random.choice(lPersonas)

oGenerador = sortear(lPersonas)

print(f"Hoy Paga: {next(oGenerador)}")