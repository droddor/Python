

with open("fichero.txt" ,"r") as fichero:
    sContenido = fichero.read()
    print(f"Total caracteres en archivo: {len(sContenido)}")
    readline = fichero.readlines()
    for linea in readline:
        print(linea)

    lCaracteres = []
    for linea in readline:
        lCaracteres = linea.split()

    print(lCaracteres)
    print(len(lCaracteres))

    for caracter in lCaracteres:
        print(caracter)