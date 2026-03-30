class GestorErrores:

    EXITO = 0

    # ERRORES PERSONA
    ERR_NOMBRE_VACIO = -1
    ERR_NOMBRE_TIPO = -2
    ERR_NOMBRE_RANGO = -3

    ERR_APELLIDO_VACIO = -4
    ERR_APELLIDO_TIPO = -5
    ERR_APELLIDO_RANGO = -6

    ERR_TELEFONO_VACIO = -7
    ERR_TELEFONO_TIPO = -8
    ERR_TELEFONO_RANGO = -9

    # ERRORES AGENDA

    ERR_RUTAFICHERO_VACIA = -10
    ERR_RUTAFICHERO_TIPO = -11
    ERR_RUTAFICHERO_RANGO = -12

    ERR_FICHERO_ESCRITURA = -13

    ERR_ALTAAGENDA_INVALIDO = -14
    ERR_ALTAAGENDA_TIPO = -15

    ## Por implementar

    _mensajes = {
        EXITO: "Operacion realizada con exito",

        # ERRORES PERSONA
        ERR_NOMBRE_VACIO: "ERROR: El nombre no puede estar vacio",
        ERR_NOMBRE_TIPO: "ERROR: El nombre debe ser tipo string",
        ERR_NOMBRE_RANGO: "ERROR: El nombre no puede superar los 100 caracteres",

        ERR_APELLIDO_VACIO: "ERROR: Los apellidos no pueden estar vacios",
        ERR_APELLIDO_TIPO: "ERROR: Los apellidos deben ser tipo string",
        ERR_APELLIDO_RANGO: "ERROR: Los apellidos no pueden superar los 100 caracteres",

        ERR_TELEFONO_VACIO: "ERROR: El telefono no puede estar vacio",
        ERR_TELEFONO_TIPO: "ERROR: El telefono debe ser tipo string",
        ERR_TELEFONO_RANGO: "ERROR: El telefono no puede superar los 100 caracteres",

        # ERRORES AGENDA

        ERR_RUTAFICHERO_VACIA: "ERROR: Ruta fichero vacio",
        ERR_RUTAFICHERO_TIPO: "ERROR: Ruta fichero tipo string",
        ERR_RUTAFICHERO_RANGO: "ERROR: Ruta fichero no puede tener mas de 100 caracteres",

        ERR_FICHERO_ESCRITURA: "ERROR: Lectura de fichero falló",

        ERR_ALTAAGENDA_INVALIDO: "ERROR: Alta en agenda invalida",
        ERR_ALTAAGENDA_TIPO: "ERROR: Alta de tipo invalido"

    }
    @staticmethod
    def getMensajeError(iCodigo):
        return GestorErrores._mensajes.get(iCodigo, "Error desconocido")