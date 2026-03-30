from EPD2.GestorErrores import GestorErrores
from EPD2.Modelo.Electrodomestico import Electrodomestico
from EPD2.Modelo.Televisor import Televisor
from EPD2.Modelo.Lavadora import Lavadora


class StockProducto():
    def __init__(self, oProducto, iStock):
        self._lErrores = []

        # Inicializamos atributos internos Privados
        self._oProducto = None
        self._iStock = 0

        # Asignacion mediante setters
        self.oProducto = oProducto
        self.iStock = iStock

    def _registrarError(self, iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    def esValido(self):
        # Es valido si stock es correcto y el producto internamente existe y es valido
        bProductoValido = (self._oProducto is not None and self._oProducto.esValido())
        return (bProductoValido and self._iStock >= 0)

    def getErrores(self):
        return self._lErrores

    def limpiarErrores(self):
        self._lErrores = []

    ## GET / SET

    @property
    def oProducto(self):
        return self._oProducto

    def oProducto(self, valor):
        iError = GestorErrores.EXITO
        # Validamos que sea un Electrodomestico (o hijo, como Lavadora/Televisor)
        if not isinstance(valor, Electrodomestico):
            iError = GestorErrores.ERR_PRODUCTO_TIPO
        elif valor is None:
             iError = GestorErrores.ERR_PRODUCTO_NULO
        else:
            self._oProducto = valor
        self._registrarError(iError)

    @property
    def iStock(self):
        return self._iStock

    @iStock.setter
    def iStock(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, int):
            iError = GestorErrores.ERR_STOCK_TIPO
        elif valor < 0:
            iError = GestorErrores.ERR_STOCK_RANGO
        else:
            self._iStock = valor
        self._registrarError(iError)

    ## TO STRING

    def __str__(self):
        if self.esValido():
            sEstado = "[OK]"
        else:
            sEstado = "[INVALID]"

        sInfoProducto = str(self._oProducto) if self._oProducto else "Sin Producto"

        return f"{sEstado} PRODUCTO: [{sInfoProducto}] - STOCK: {self._iStock} uds."