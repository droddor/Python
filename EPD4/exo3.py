with open("fichero.txt" , "r") as fichero:
    lineas = fichero.readlines()
    print(f"El fichero tiene {len(lineas)} lineas")