class GestorErrores:

    """
    Este codigo es necesario implementarlo en cualquier ejercicio que hagamos,
    ya que hay que hacer validaciones de los datos y sera indispensable implementarlo en nuestro codigo. ES IMPORTANTE
    """


    EXITO = 0

    # ERRORES COMUNES ==============================

    # NOMBRE - (Usado en Estudiante y Electrodomestico)

    ERR_NOMBRE_TIPO = -3
    ERR_NOMBRE_LONGITUD = -4
    ERR_NOMBRE_VACIO = -5

    # ERRORES ELECTRODOMESTICO ======================
    # PRECIO
    ERR_PRECIO_TIPO = -12
    ERR_PRECIO_RANGO = -13

    # ERRORES LAVADORA ==============================
    # CARGA
    ERR_CARGA_TIPO = -14
    ERR_CARGA_RANGO = -15

    # ERRORES TELEVISOR =============================
    # PULGADAS
    ERR_PULGADAS_TIPO = -16
    ERR_PULGADAS_RANGO = -17

    # FULLHD
    ERR_FULLHD_TIPO = -18

    # ERRORES STOCK (CANTIDAD) =====================
    # OBJETO PRODUCTO
    ERR_PRODUCTO_TIPO = -19
    ERR_PRODUCTO_NULO = -20

    # STOCK
    ERR_STOCK_TIPO = -21
    ERR_STOCK_RANGO = -22

    # ERRORES ALMACEN ==============================
    # LISTAS INTERNAS
    ERR_ALMACEN_CATALOGO_TIPO = -23
    ERR_ALMACEN_STOCK_TIPO = -24

    # OPERACIONES ALTA/ENTRADA
    ERR_ALMACEN_ALTA_YA_EXISTE = -25
    ERR_ALMACEN_ALTA_TIPO_INVALIDO = -26
    ERR_ALMACEN_NO_CATALOGADO = -27 # operar con algo que no esta en catalogo
    ERR_ALMACEN_UNIDADES_RANGO = -28 # meter/sacar cantidad negativa o cero

    # OPERACIONES SALIDA
    ERR_ALMACEN_NO_STOCK = -29 # En catalogo pero no en stock 0
    ERR_ALMACEN_STOCK_INSUFICIENTE = -30 # Intentar sacar mas cantidad de lo que hay en stock

    """
    AQUI GUARDAREMOS LOS MENSAJES DE ERROR DE CADA UNO DE ELLOS
    
    """
    # DICCIONARIO
    _mensajes = {
        EXITO: "Operacion realizada con éxito",

        # ERRORES COMUNES ==============================
        ERR_NOMBRE_TIPO: "ERROR: El nombre debe ser un string",
        ERR_NOMBRE_LONGITUD: "ERROR: El nombre supera los 100 caracteres",
        ERR_NOMBRE_VACIO: "ERROR: El nombre no puede estar vacio",

        # ERRORES ELECTRODOMESTICO ======================
        # PRECIO
        ERR_PRECIO_TIPO: "ERROR: El precio debe ser un numero int/float",
        ERR_PRECIO_RANGO: "ERROR: El precio no puede ser negativo",

        # ERRORES LAVADORA ==============================
        # CARGA
        ERR_CARGA_TIPO: "ERROR: La carga debe ser un numero int/float",
        ERR_CARGA_RANGO: "ERROR: La carga debe ser mayor que cero",

        # ERRORES TELEVISOR =============================
        # PULGADAS
        ERR_PULGADAS_TIPO: "ERROR: Las pulgadas debe ser un numero int/float",
        ERR_PULGADAS_RANGO: "ERROR: Las pulgadas debe ser mayor que cero",

        # FULLHD
        ERR_FULLHD_TIPO: "ERROR: El indicador FULLHD debe ser booleano",

        # ERRORES STOCK (CANTIDAD) =====================
        # OBJETO PRODUCTO
        ERR_PRODUCTO_TIPO: "ERROR: El objeto producto debe ser de tipo Electrodomestico o derivado",
        ERR_PRODUCTO_NULO: "ERROR: No se ha asignado ningun producto (Es None)",

        # STOCK
        ERR_STOCK_TIPO: "ERROR: El stock debe ser un numero entero",
        ERR_STOCK_RANGO: "ERROR: El stock no puede ser negativo",

        # ERRORES ALMACEN ==============================
        # LISTAS INTERNAS
        ERR_ALMACEN_CATALOGO_TIPO: "ERROR: El catalogo debe ser una lista",
        ERR_ALMACEN_STOCK_TIPO: "ERROR: El stock debe ser una lista",

        # OPERACIONES ALTA/ENTRADA
        ERR_ALMACEN_ALTA_YA_EXISTE: "ERROR: El Electrodomestico ya existe en el catalogo",
        ERR_ALMACEN_ALTA_TIPO_INVALIDO: "ERROR: Solo se pueden añadir objetos de tipo Electrodomestico al catalogo",
        ERR_ALMACEN_NO_CATALOGADO: "ERROR: El producto no existe en el catalogo",
        ERR_ALMACEN_UNIDADES_RANGO: "ERROR: Las unidades deben ser mayor que cero",

        # OPERACIONES SALIDA
        ERR_ALMACEN_NO_STOCK: "ERROR: No existe registro de stock para este producto",
        ERR_ALMACEN_STOCK_INSUFICIENTE: "ERROR: No hay suficiente stock de este producto",
    }
    # DEFINIMOS METODO PARA DEVOLVER EL ERROR, QUE RECIBIRA UN ENTERO DE LOS QUE HEMOS PUESTO DESDE -2 A -30 Y DEVOLVERA EL ERROR ASOCIADO AL CODIGO
    @staticmethod
    def getMensajeError(iCodigo):
        return GestorErrores._mensajes.get(iCodigo, "ERROR: DESCONOCIDO")