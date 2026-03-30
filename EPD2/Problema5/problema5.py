import csv
from tabulate import tabulate

def cargarCsv():
    dVinos = {}
    with open ("VinoBlanco.csv", "r", encoding="utf-8-sig") as csvfile:
        # oLector = csv.reader(csvfile) con esto se trata el csv con filas
        oLector = csv.DictReader(csvfile)
        for fila in oLector:

            sKey = fila["Name"] # Obtenermos la clave. En vez de hacer que la sea cada columna, usamos una columna como clave unica para tratar el diccionario.

            #Year tiene datos no numericos para indicar año desconocido. Pondremos none.
            iYear = int(fila["Year"]) if fila["Year"] != "N.V." else None
            #Los demas datos seran una tupla que se corresponda con la key
            # hay que convertir los datos, ya que al tratarlos en un diccionario se convierten en str
            tVino = (
                fila["Name"],
                fila["Country"],
                fila["Region"],
                fila["Winery"],
                float(fila["Rating"]),
                int(fila["NumberOfRatings"]),
                float(fila["Price"]),
                iYear
            )
            dVinos[sKey] = tVino
    return dVinos

def buscarRegistro(dVinos):
    sClave = input("Ingrese el nombre que desea buscar: ")
    if sClave in dVinos:
        print("="*10 + " Registro encontrado " + "="*10)
        tVino = dVinos[sClave]
        print(f"Name: {tVino[0]}")
        print(f"Country: {tVino[1]}")
        print(f"Region: {tVino[2]}")
        print(f"Winery: {tVino[3]}")
        print(f"Rating: {tVino[4]}")
        print(f"NumberOfRatings: {tVino[5]}")
        print(f"Price: {tVino[6]} $")
        print(f"Year: {tVino[7]}")
        return sClave
    else:
        print("Vino no encontrado en directorio")
        return None

def borrarRegistro(dVinos):
    sClave = buscarRegistro(dVinos)
    if sClave is not None:
        borrar = input("Confirme, desea borrar el registro? (y/n): ")
        if borrar.lower() == "y":
            del dVinos[sClave]
            print("Registro borrado")
        elif borrar.lower() == "n":
            print("Operacion cancelada")
    else:
        print("Vino no encontrado en directorio")

def agregarRegistro(dVinos):
    sName = input("Introduce el valor del campo Name: ")
    if sName in dVinos:
        print("El Name ya existe en el registro")
        return None
    else:
        sCountry = input("Introduce el valor del campo Country: ")
        sRegion = input("Introduce el valor del campo Region: ")
        sWinery = input("Introduce el valor del campo Winery: ")
        fRating = float(input("Introduce el valor del campo Rating: "))
        iNumberOfRatings = int(input("Introduce el valor del campo NumberOfRatings: "))
        fPrice = float(input("Introduce el valor del campo Price: "))
        iYear = int(input("Introduce el valor del campo Year: "))

        tVino = (sName,sCountry,sRegion,sWinery,fRating,iNumberOfRatings,fPrice,iYear)

        dVinos[sName] = tVino
        print(f"Registro agregado correctamente {tVino}")

def listarRegistrosTabla(dVinos):
    if len(dVinos)==0:
        print("No hay registros")
        return

    lFilas = list(dVinos.values())
    lColumnas = ["Name","Country","Region","Winery","Rating","NumberOfRatings","Price","Year"]
    print(tabulate(lFilas, headers=lColumnas, tablefmt="pipe"))

def mostrarMenu():
    print("\n")
    print("="*10 + " MENU REGISTRO VITICOLA "+"="*10)
    print("=" * 44)
    print("1. Agregar registro")
    print("2. Buscar registro por su clave y mostrar valores")
    print("3. Borrar registro a partir de su clave")
    print("4. Mostrar registros en formato tabla")
    print("5. Salir")
    print("="*44)

if __name__=="__main__":

    dVinos = cargarCsv()

    while True:
        mostrarMenu()
        try:
            iOpcion = int(input("Seleccione Opcion: "))

            if iOpcion == 1:
                agregarRegistro(dVinos)
            elif iOpcion == 2:
                buscarRegistro(dVinos)
            elif iOpcion == 3:
                borrarRegistro(dVinos)
            elif iOpcion == 4:
                listarRegistrosTabla(dVinos)
            elif iOpcion == 5:
                print("Saliendo...")
                break
            else:
                print("Opcion no valida")
        except ValueError:
            print("Opcion no valida, Introduce una opcion valida")
