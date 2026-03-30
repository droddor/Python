from GestorErrores.GestorErrores import GestorErrores
from Modelo.FiltroAire import FiltroAire
from Modelo.GestorFiltros import GestorFiltros

# Metodo para mostrar errores - Gestor Errores
def mostrarErrores(oErrores):
    if len(oErrores.getErrores()) > 0:
        print("ERRORES DETECTADOS:")
        for iCodigo in oErrores.getErrores():
            print(f"{GestorErrores.getMensajeError(iCodigo)}")
        oErrores.limpiarErrores()


if __name__ == "__main__":
    # Creamos Objeto Gestor y cargamos datos desde sRutaFichero o desde sRutaCSV si no se ha generado otro
    print("--- PRUEBA CARGAR FICHERO ---")
    oGestorFiltros = GestorFiltros("FiltrosP2.json","2_air_filter.csv")
    oGestorFiltros._comprobarFichero()
    print(oGestorFiltros)

    # PRUEBA AÑADIR
    print("\n--- PRUEBA AÑADIR ---")
    oFiltro1 = FiltroAire(44197,"TEST_NombreFiltro_1","Test_localizacion1","Test_Class1",
                    5,0.1,0.2,0.3,
                    0.4,0.5,0.6,0.7,False,12)
    print(oGestorFiltros.añadir(oFiltro1))
    mostrarErrores(oGestorFiltros)

    # PRUEBA AÑADIR REGISTRO INVALIDO
    print("\n--- PRUEBA AÑADIR REGISTRO INVALIDO ---")
    oFiltroInvalido = FiltroAire(123,"","","",
                    5,0.1,0.2,0.3,
                    0.4,0.5,0.6,0.7,False,12)
    oGestorFiltros.añadir(oFiltroInvalido)
    mostrarErrores(oGestorFiltros)
    mostrarErrores(oFiltroInvalido)

    # PRUEBA DUPLICADO
    print("\n--- PRUEBA DUPLICADO ---")
    print(oGestorFiltros.añadir(oFiltro1))

    # GUARDAR DATOS EN FICHERO
    print("\n--- PRUEBA GUARDAR DATOS EN FICHERO ---")
    oGestorFiltros.guardarFichero()
    print(oGestorFiltros)

    # PRUEBA BUSCAR - Probamos con registro añadido y con otro existente - Clave: id + Nombre + hora
    print("\n--- PRUEBA BUSQUEDA (2 Busquedas) ---")
    tClave = (44197,"TEST_NombreFiltro_1",12)
    tClave2 = (44540,"AHU_Filter_Office",1)
    print(oGestorFiltros.buscar(tClave))
    print(oGestorFiltros.buscar(tClave2))

    # PRUEBA BUSCAR POR RANGO - Buscamos otros registros que cumplan condicion rango en campo
    print("\n--- PRUEBA BUSQUEDA POR RANGO ---")
    lResultados = oGestorFiltros.buscarPorRango("fEfficiency",0.99,1.0)
    print(f"Registros encontrados en rango indicado: {len(lResultados)}")

    for oFiltro in lResultados:
        print(oFiltro)

    # PRUEBA ELIMINAR
    print("\n--- PRUEBA ELIMINAR ---")
    print(oGestorFiltros.eliminar(tClave))
    # PRUEBA ELIMINAR DATO INEXISTENTE
    print("\n--- PRUEBA ELIMINAR INEXISTENTE ---")
    print(oGestorFiltros.eliminar(tClave))

    # PRUEBA BUSCAR EL REGISTRO DE PRUEBA
    print("\n--- PRUEBA BUSQUEDA ---")
    tClave = (44197, "TEST_NombreFiltro_1", 12)
    print(oGestorFiltros.buscar(tClave))

    # PRUEBA GUARDAR CAMBIOS FINALES
    print("\n--- PRUEBAGUARDAR CAMBIOS FINALES ---")
    oGestorFiltros.guardarFichero()
    print("\nCambios guardados correctamente")
    print(oGestorFiltros)

