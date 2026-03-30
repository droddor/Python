with open("fichero.txt", "r") as fichero:
    sContenido = fichero.read()

dOcurrencias = {}
for sCaracter in sContenido:
    if sCaracter in dOcurrencias:
        dOcurrencias[sCaracter] += 1
    else:
        dOcurrencias[sCaracter] = 1

print(dOcurrencias)

for i in sContenido:
    print(i)

with open("fichero.txt", "r") as fichero:
    iCaracteres = fichero.read()
    contador = 0
    for i in iCaracteres:
    #letra = i.split()
        if i == "a":
            contador += 1

    print(f"El nuermo de 'A' en el fichero es : {contador}")