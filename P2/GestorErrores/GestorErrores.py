class GestorErrores:
    EXITO = 0

    # ERRORES ID

    ERR_ID_TIPO = -1
    ERR_ID_RANGO = -2

    # ERRORES FILTRO STR

    ERR_FILTER_NAME_TIPO = -3
    ERR_FILTER_NAME_VACIO = -4
    ERR_FILTER_NAME_RANGO = -5

    ERR_FILTER_LOCATION_TIPO = -6
    ERR_FILTER_LOCATION_VACIO = -7
    ERR_FILTER_LOCATION_RANGO = -8

    ERR_FILTER_CLASS_TIPO = -9
    ERR_FILTER_CLASS_VACIO = -10
    ERR_FILTER_CLASS_RANGO = -11

    # ERRORES FILTRO VALORES NUMERICOS

    ERR_FILTER_AGE_TIPO = -12

    ERR_FILTER_FACTOR_TIPO = -13

    ERR_FILTER_PRES_TIPO = -14

    ERR_FILTER_EFI_TIPO = -15

    ERR_FILTER_PM_TIPO = -16

    ERR_FILTER_REPLACE_TIPO = -17

    ERR_FILTER_HORA_TIPO = -18
    ERR_FILTER_HORA_RANGO = -19

    # ERRORES FICHERO

    ERR_RUTA_FICHERO_TIPO = -20
    ERR_RUTA_FICHERO_VACIO = -21

    # ERRORES GESTOR FILTROS

    ERR_FILTER_TIPO = -22
    ERR_FILTER_INVALIDO = -23


    # Diccionario de mensajes para cada error
    _mensajes = {

        EXITO: "Datos introducidos con éxito",

        # ERRORES ID

        ERR_ID_TIPO: "El id tiene que ser de tipo entero",
        ERR_ID_RANGO: "El id tiene que estar dentro del rango (10000-99999)",

        # ERRORES FILTRO STR

        ERR_FILTER_NAME_TIPO: "El campo nombre tiene que ser de tipo string",
        ERR_FILTER_NAME_VACIO: "El campo nombre no puede estar vacio",
        ERR_FILTER_NAME_RANGO: "El campo nombre no puede contener mas de 100 caracteres",

        ERR_FILTER_LOCATION_TIPO: "El campo localizacion tiene que ser de tipo string",
        ERR_FILTER_LOCATION_VACIO: "El campo localizacion no puede estar vacio",
        ERR_FILTER_LOCATION_RANGO: "El campo localizacion no puede tener mas de 100 caracteres",

        ERR_FILTER_CLASS_TIPO: "El campo clase de filtro debe ser string",
        ERR_FILTER_CLASS_VACIO: "El campo clase de filtro no puede estar vacio",
        ERR_FILTER_CLASS_RANGO: "El campo clase de filtro no puede contener mas de 100 caracteres",

        # ERRORES FILTRO VALORES NUMERICOS

        ERR_FILTER_AGE_TIPO: "El campo edad del filtro debe ser de tipo numerico",

        ERR_FILTER_FACTOR_TIPO: "El campo factor debe ser de tipo numerico",

        ERR_FILTER_PRES_TIPO: "El campo presion del filtro debe ser de tipo numerico",

        ERR_FILTER_EFI_TIPO: "El campo eficiencia del filtro debe ser de tipo numerico",

        ERR_FILTER_PM_TIPO: "El campo PM del filtro debe ser de tipo numerico",

        ERR_FILTER_REPLACE_TIPO: "El campo reemplazar del filtro debe ser de tipo bool (True/False)",

        ERR_FILTER_HORA_TIPO: "El campo hora medicion del filtro debe ser de tipo entero",
        ERR_FILTER_HORA_RANGO: "El campo hora medicion del filtro debe estar entre (0-23) horas",

        # ERRORES FICHERO

        ERR_RUTA_FICHERO_TIPO: "La ruta del fichero debe ser de tipo string",
        ERR_RUTA_FICHERO_VACIO: "La ruta del fichero no puede estar vacia",

        # ERRORES GESTOR FILTROS

        ERR_FILTER_TIPO: "El objeto debe ser de tipo FiltroAire",
        ERR_FILTER_INVALIDO: "El objeto FiltroAire es INVALIDO",


    }

    # Metodo estatico para devolver mensaje de error despues de identificar codigo o default
    @staticmethod
    def getMensajeError(iCodigo):
        return GestorErrores._mensajes.get(iCodigo, "Error desconocido.")

