from EPD2.GestorErrores import GestorErrores

class Electrodomestico:
    def __init__(self,sNombre,fPrecio):

        self._lErrores = [] # Lista de errores recogidos

        # Inicializar valores de atributos por defecto
        self._sNombre = ""
        self._fPrecio = 0.0

        # Asignar valores del constructor para get/set
        self.sNombre = sNombre
        self.fPrecio = fPrecio

    def _registrarError(self, iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    def esValido(self):
        return (self._sNombre != "") and (self._fPrecio > 0)

    def getErrores(self):
        return self._lErrores

    def limpiarErrores(self):
        self._lErrores = []

    ## GET / SET

    @property
    def sNombre(self):
        return self._sNombre

    @sNombre.setter
    def sNombre(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor,str):
            iError = GestorErrores.ERR_NOMBRE_TIPO
        elif len(valor) == 0:
            iError = GestorErrores.ERR_NOMBRE_VACIO
        else:
            self._sNombre = valor
        self._registrarError(iError)

    @property
    def fPrecio(self):
        return self._fPrecio

    @fPrecio.setter
    def fPrecio(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor,(int,float)):
            iError = GestorErrores.ERR_PRECIO_TIPO
        elif valor < 0:
            iError = GestorErrores.ERR_PRECIO_RANGO
        else:
            self._fPrecio = float(valor) ## gestionar errores/ validaciones
        self._registrarError(iError)

    def __eq__(self, oOther):
        if isinstance(oOther,Electrodomestico): # comparas por nombre y precio los electrodomesticos
            return (self._sNombre == oOther.sNombre and self._fPrecio == oOther.fPrecio)
        return False

    ## TO STRING
    def __str__(self):
        sPrecioFormateado = f"{self._fPrecio:.2f}"  # Formato de precio con 2 decimales

        if self.esValido():
            sEstado = "[OK]"
        else:
            sEstado = "[INVALIDO]"

        return f"{sEstado} {self._sNombre} - {sPrecioFormateado}€"