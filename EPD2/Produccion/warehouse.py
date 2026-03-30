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


from EPD2.GestorErrores import GestorErrores
from EPD2.Modelo.Electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):
    def __init__(self, sNombre, fPrecio, fCarga):
        super().__init__(sNombre, fPrecio) # inicializar desde padre

        self._fCarga = 0.0

        self.fCarga = fCarga

    def esValido(self):
        return super().esValido() and self._fCarga > 0 # Es valida si Padre Electrodomestsico lo es. y la garga es mayor que cero

    @property
    def fCarga(self):
        return self._fCarga

    @fCarga.setter
    def fCarga(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor,(int,float)): # dato y validaciones
            iError = GestorErrores.ERR_CARGA_TIPO
        elif valor <= 0:
            iError = GestorErrores.ERR_CARGA_RANGO
        else:
            self._fCarga = float(valor)
        self._registrarError(iError) # Metodo heredado de electrodomestico para registrar error

    def __str__(self):
        return f"{super().__str__()} - Carga: {self._fCarga} KG"

from EPD2.GestorErrores import GestorErrores
from EPD2.Modelo.Electrodomestico import Electrodomestico


class Televisor(Electrodomestico):
    def __init__(self, sNombre, fPrecio, fPulgadas, bFullHD):
        super().__init__(sNombre, fPrecio) # inicializar atributos desde padre

        #Atributos inicializados por defecto. LOS PRIVADOS SON INICIALIZADOS SIEMPRE
        self._fPulgadas = 0.0
        self._bFullHD = False

        #Atributos inicializados desde constructor
        self.fPulgadas = fPulgadas
        self.bFullHD = bFullHD

    def esValido(self):
        return super().esValido() and self._fPulgadas > 0

    @property
    def fPulgadas(self):
        return self._fPulgadas

    @fPulgadas.setter
    def fPulgadas(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor,(int, float)):
            iError = GestorErrores.ERR_PULGADAS_TIPO
        elif valor <= 0:
            iError = GestorErrores.ERR_PULGADAS_RANGO
        else:
            self._fPulgadas = float(valor)
        self._registrarError(iError)

    @property
    def bFullHD(self):
        return self._bFullHD

    @bFullHD.setter
    def bFullHD(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor,bool):
            iError = GestorErrores.ERR_FULLHD_TIPO
        else:
            self._bFullHD = valor
        self._registrarError(iError)

    def __str__(self):
        sTextoFullHD = "SI" if self._bFullHD else "NO"
        return f"{super().__str__()} - {self._fPulgadas} - FullHD: {sTextoFullHD}"

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

    @oProducto.setter
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

from EPD2.GestorErrores import GestorErrores
from EPD2.Modelo import Electrodomestico, Televisor, Lavadora, StockProducto


class Almacen:
    def __init__(self):
        self._lErrores = []

        # inicializacion de atributos. No hay constructor, por lo que solo los añadimos para get/set
        self._lCatalogo = []
        self._lStock = []

    def _registrarError(self, iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lCatalogo.append(iCodigo)

    def esValido(self):
        # Almacen valido si no hay errores en las operaciones
        return len(self._lCatalogo) == 0

    def getErrores(self):
        return self._lErrores

    def limpiarErrores(self):
        self._lErrores = []

    # GET / SET de los atributos

    @property
    def lCatalogo(self):
        return self._lCatalogo

    @lCatalogo.setter
    def lCatalogo(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, list):
            iError = GestorErrores.ERR_ALMACEN_CATALOGO_TIPO
        else:
            self._lCatalogo = valor
        self._registrarError(iError)

    @property
    def lStock(self):
        return self._lStock

    @lStock.setter
    def lStock(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, list):
            iError = GestorErrores.ERR_STOCK_TIPO
        else:
            self._lStock = valor
        self._registrarError(iError)


    # METODOS

    # Insertar en catalogo ==================
    def altaCatalogo(self, oElectro):
        bInsertado = False
        iError = GestorErrores.EXITO

        if not isinstance(oElectro, Electrodomestico):
            iError = GestorErrores.ERR_ALMACEN_ALTA_TIPO_INVALIDO
        else:
            if self._buscarElectroCatalogo(oElectro) is None:
                self._lCatalogo.append(oElectro)
                bInsertado = True
            else:
                iError = GestorErrores.ERR_ALMACEN_ALTA_YA_EXISTE
        self._registrarError(iError)
        return bInsertado

    def _buscarElectroCatalogo(self, oElectro):
        oElectroEncontrado = None
        for oElec in self.lCatalogo:
            if oElec.sNombre == oElectro.sNombre:
                oElectroEncontrado = oElec
                break
        return oElectroEncontrado

    def entradaStock(self, sNombre, iUnidades):
        # Validacion inicial
        if iUnidades <= 0:
            self._registrarError(GestorErrores.ERR_ALMACEN_UNIDADES_RANGO)
            return f" {GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_UNIDADES_RANGO)} "
        oElectroDummy = Electrodomestico(sNombre,1)
        oElectro = self._buscarElectroCatalogo(oElectroDummy)
        sSalida = " "

        if oElectro is None:
            self._registrarError(GestorErrores.ERR_ALMACEN_NO_CATALOGADO)
            sSalida = {GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_NO_CATALOGADO)}
        else:
            oStockProducto = self._buscarStockElectro(oElectro)

            if oStockProducto is None:
                oStockProducto = StockProducto(oElectro, iUnidades)
                self.lStock.append(oStockProducto)
                sSalida = f"Unidades agregadas al stock del producto: {oStockProducto.oProducto.sNombre}"

            else:
                oStockProducto.iStock += iUnidades
                sSalida = f"Unidades incrementadas al stock del producto: {oStockProducto.oProducto.sNombre}"

        return sSalida

    def _buscarStockElectro(self, oElectro):
        oStockEncontrado = None
        for oStock in self.lStock:
            if oStock.oProducto.sNombre == oElectro.sNombre:
                oStockEncontrado = oStock
                break
        return oStockEncontrado


    def salidaStock(self, sNombre, iUnidades):
        # Validacion inicial
        if iUnidades <= 0:
            self._registrarError(GestorErrores.ERR_ALMACEN_UNIDADES_RANGO)
            return f"{GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_UNIDADES_RANGO)}"

        oElectroDummy = Electrodomestico(sNombre,1)
        oElectro = self._buscarElectroCatalogo(oElectroDummy)

        sSalida = " "

        if oElectro is None:
            self._registrarError(GestorErrores.ERR_ALMACEN_NO_CATALOGADO)
            sSalida = {GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_NO_CATALOGADO)}
        else:
            oStockProducto = self._buscarStockElectro(oElectro)

            if oStockProducto is None:
                self._registrarError(GestorErrores.ERR_ALMACEN_NO_STOCK)
                sSalida = {GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_NO_STOCK)}
            else:
                if oStockProducto.isStock < iUnidades:
                    self._registrarError(GestorErrores.ERR_ALMACEN_STOCK_INSUFICIENTE)
                    sSalida = f"No hay Stock suficiente del producto: {oStockProducto.oProducto.sNombre}"
                    sSalida += f"Stock actual: {oStockProducto.iStock}"

                elif oStockProducto.isStock > iUnidades:
                    oStockProducto.iStock -= iUnidades
                    sSalida = f"Unidades decrementadas al stock del producto: {oStockProducto.oProducto.sNombre}"

                else:
                    #Caso stock se queda a cero
                    self.lStock.remove(oStockProducto)
                    sSalida = f"Unidades decrementadas al stock del producto: {oStockProducto.oProducto.sNombre}"
                    sSalida += f" Ya no quedan existencias (Eliminado de stock)"

        return sSalida

    def listadoCatalogo(self):
        sListado = "" if len(self.lCatalogo) > 0 else "No hay datos que mostrar"
        for oProducto in self.lCatalogo:
            sListado += str(oProducto) + "\n"
        return sListado

    def listadoStock(self):
        sListado = "" if len(self.lStock) > 0 else "No hay datos que mostrar"
        for oStockProducto in self.lStock:
            sListado += str(oStockProducto) + "\n"
        return sListado

    def numTelevisoresStock(self):
        iTotalTV = 0
        for oStockProducto in self.lStock:
            if isinstance(oStockProducto.oProducto, Televisor):
                iTotalTV += oStockProducto.iStock
        return iTotalTV

    def numLavadorasStock(self):
        iTotalLavadoras = 0
        for oStockProducto in self.lStock:
            if isinstance(oStockProducto.oProducto, Lavadora):
                iTotalLavadoras += oStockProducto.iStock
        return iTotalLavadoras

    def importeTotalStock(self):
        fTotalImporte = 0.0
        for oStockProducto in self.lStock:
            fTotalImporte += oStockProducto.oProducto.fPrecio * oStockProducto.iStock
        return fTotalImporte

    def __str__(self):
        sEstado = "[OK]" if self.esValido() else "[INVALID]"
        return f"{sEstado} Almacen con {len(self.lCatalogo)} productos en catalogo y {len(self.lStock)} referencias en stock."