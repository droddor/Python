from EPD2.Problema1.GestorErrores.GestorErrores import GestorErrores

class Persona:
    def __init__(self, sNombre, sApellido, sTelefono):
        self._lErrores = []

        """
        Es importante inicializar los atributos privados.
        Los atributos publicos seran vistos desde el setter/Getter y despues de pasar la validacion, se cambiara el atributo privado
        """

        # Inicializacion de atributos privados, para modificar despues de validar
        self._sNombre = ""
        self._sApellido = ""
        self._sTelefono = ""

        # Para asignar mediante setter y activar validaciones
        self.sNombre = sNombre
        self.sApellido = sApellido
        self.sTelefono = sTelefono


    # GESTION DE ERRORES

    # Metodo para registrar Error
    def _registrarError(self,iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    # Metodo para mostrar Errores
    def getErrores(self):
        return self._lErrores

    def limpiarErrores(self):
        self._lErrores = []

    def esValido(self):
        return (self._sNombre != "" and
                self._sApellido != "" and
                self._sTelefono != "")

    # GETTERS / SETTERS

    @property
    def sNombre(self):
        return self._sNombre

    # El setter lo pasamos por el gestor de errores para validar.
    @sNombre.setter
    def sNombre(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str): # si el dato no es de tipo str...
            iError = GestorErrores.ERR_NOMBRE_TIPO
        elif len(valor) > 100:
                iError = GestorErrores.ERR_NOMBRE_RANGO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_NOMBRE_VACIO
        else:
            self._sNombre = valor
        self._registrarError(iError)

    @property
    def sApellido(self):
        return self._sApellido

    # El setter lo pasamos por el gestor de errores para validar.
    @sApellido.setter
    def sApellido(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):  # si el dato no es de tipo str...
            iError = GestorErrores.ERR_APELLIDO_TIPO
        elif len(valor) > 100:
            iError = GestorErrores.ERR_APELLIDO_RANGO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_APELLIDO_VACIO
        else:
            self._sApellido = valor
        self._registrarError(iError)

    @property
    def sTelefono(self):
        return self._sTelefono

    # El setter lo pasamos por el gestor de errores para validar.
    @sTelefono.setter
    def sTelefono(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):  # si el dato no es de tipo str...
            iError = GestorErrores.ERR_TELEFONO_TIPO
        elif len(valor) > 100:
            iError = GestorErrores.ERR_TELEFONO_RANGO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_TELEFONO_VACIO
        else:
            self._sTelefono = valor
        self._registrarError(iError)

    def mostrarErrores(oObjeto):
        if len(oObjeto.getErrores()) > 0:
            print("[!] ERRORES DETECTADOS:")
            for iCodigo in oObjeto.getErrores():
                print(f"  -> {GestorErrores.getMensajeError(iCodigo)}")
            oObjeto.limpiarErrores()

    def __str__(self):
        return f"{self._sNombre} {self._sApellido} {self._sTelefono}"
