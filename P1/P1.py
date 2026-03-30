import os
import sys
import time

#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','P2'))

from GestorErrores.GestorErrores import GestorErrores
from Modelo.FiltroAire import FiltroAire
from Modelo.GestorFiltros import GestorFiltros
from tabulate import tabulate



# FiltrosP1.json se creara en la raiz del Paquete P1 si se ha generado un archivo
# El CSV lo leera del Paquete P2
_RUTA_P1 = os.path.abspath(os.path.dirname(__file__))
RUTA_JSON = os.path.join(_RUTA_P1, "FiltrosP1.json")
RUTA_CSV = os.path.join(_RUTA_P1,"..","P2", "2_air_filter.csv")

# Metodo para mostrar errores - Gestor Errores
def mostrarErrores(oErrores):
    if len(oErrores.getErrores()) > 0:
        print("ERRORES DETECTADOS:")
        for iCodigo in oErrores.getErrores():
            print(f"{GestorErrores.getMensajeError(iCodigo)}")
        oErrores.limpiarErrores()

# Metodo para hacer uso de tabulate cuando sea necesario
def mostarFormatoTabla(lFiltros):
    if not lFiltros:
        print("Sin resultados.")
        return
    lDatos = [oFiltro.toDict() for oFiltro in lFiltros]
    print(tabulate(lDatos, headers="keys", tablefmt="grid"))
    print(f"Total: {len(lFiltros)} registros.")

if __name__ == "__main__":
    # Inicio menu - Bienvenida + carga de datos

    print("\n")
    print("#"*22 + " BIENVENIDO " +"#"*22 )
    print("Cargando datos, por favor espere ........")
    time.sleep(2)

    # Creamos objeto gestor y pasamos ruta ficheros a gestor de filtros para cargarlos
    oGestor = GestorFiltros(RUTA_JSON, RUTA_CSV)

    # Comprobamos si existe un fichero ya generado (editado de csv)
    oGestor._comprobarFichero()

    # Llamamos a Str de GestorFichero
    print(oGestor)

    bSalir = False
    while not bSalir:
        print("\n" + "=" * 50)
        print("     SISTEMA DE GESTION DE FILTROS DE AIRE")
        print("=" * 50)
        print(" 1. Añadir nuevo registro")
        print(" 2. Buscar registro por clave")
        print(" 3. Eliminar registro por clave")
        print(" 4. Buscar registros por rango de campo")
        print(" 5. Listar todos los registros")
        print(" 0. Guardar y salir")
        print("=" * 50)

        sOpcion = input(" Selecciona una opcion: ").strip()


        if sOpcion == "1":
            print("--- Añadir Registro ---")
            try:
                iId = int(input("ID (10000-99999): "))
                sFilterName = input("Nombre del filtro: ")
                sFilterLocation = input("Localizacion: ")
                sFilterClass = input("Clase de filtro: ")
                fFilterAgeDays = float(input("Edad en dias: "))
                fLoadFactor = float(input("Factor de carga: "))
                fPreassure = float(input("Presion (Pa): "))
                fEfficiency = float(input("Eficiencia: "))
                fInPm25 = float(input("PM2.5 entrada: "))
                fOutPm25 = float(input("PM2.5 salida: "))
                fInPm10 = float(input("PM10 entrada: "))
                fOutPm10 = float(input("PM10 salida: "))
                bReplaceNeeded = bool(int(input("Necesita reemplazo (0 = No / 1 = Si): ")))
                iHour = int(input("Hora de medicion (0-23): "))
            except ValueError:
                print("[ERROR] El dato introducido no es valido")
                continue

            oFiltro = FiltroAire(
                iId, sFilterName, sFilterLocation,sFilterClass,
                fFilterAgeDays,fLoadFactor,fPreassure,fEfficiency,
                fInPm25,fOutPm25,fInPm10,fOutPm10,bReplaceNeeded,iHour)
            mostrarErrores(oFiltro)
            print(oGestor.añadir(oFiltro))
            mostrarErrores(oGestor)


        elif sOpcion == "2":
            print("\n--- Buscar Registro ---")
            try:
                iId = int(input("ID: "))
                sNombre = input("Nombre del filtro: ")
                iHora = int(input("Hora (0-23): "))
            except ValueError:
                print("[ERROR] El dato introducido no es valido")
                continue

            tClave = (iId, sNombre, iHora)
            oResultado = oGestor.buscar(tClave)
            mostarFormatoTabla([oResultado])


        elif sOpcion == "3":
            print("\n--- Eliminar Registro ---")
            try:
                iId = int(input("ID: "))
                sNombre = input("Nombre del filtro: ")
                iHora = int(input("Hora (0-23): "))
            except ValueError:
                print("[ERROR] El dato introducido no es valido")
                continue

            tClave = (iId, sNombre, iHora)
            print(oGestor.eliminar(tClave))

        elif sOpcion == "4":
            print("\n--- Buscar por rango ---")
            print("Campos disponibles: iId, fFilterAgeDays, fLoadFactor,")
            print("fPreassure, fEfficiency, fInPm25, fOutPm25, fInPm10, fOutPm10, iHour")
            sCampo = input("\nIntroduzca campo elegido: ")
            try:
                valor1_inicial = float(input("Valor minimo: "))
                valor2_final = float(input("Valor maximo: "))
            except ValueError:
                print("[ERROR] El dato introducido no es valido")
                continue
            lResultados = oGestor.buscarPorRango(sCampo,valor1_inicial,valor2_final)
            mostarFormatoTabla(lResultados)


        elif sOpcion == "5":
            print("\n --- Mostrar Registros ---")
            lTodos = list(oGestor._dFiltros.values())
            if not lTodos:
                print("No hay registros cargados")
            else:
                mostarFormatoTabla(lTodos)

        elif sOpcion == "0":
            oGestor.guardarFichero()
            print("Cambios guardados corectamente")
            print(oGestor)
            bSalir = True
        else:
            print("[ERROR] Opcion invalida")

