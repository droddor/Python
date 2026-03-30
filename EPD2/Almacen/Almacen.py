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
            self._lErrores.append(iCodigo)

    def esValido(self):
        # Almacen valido si no hay errores en las operaciones
        return len(self._lErrores) == 0

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
            sSalida = GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_NO_CATALOGADO)
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
            sSalida = GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_NO_CATALOGADO)
        else:
            oStockProducto = self._buscarStockElectro(oElectro)

            if oStockProducto is None:
                self._registrarError(GestorErrores.ERR_ALMACEN_NO_STOCK)
                sSalida = sSalida = GestorErrores.getMensajeError(GestorErrores.ERR_ALMACEN_NO_STOCK)
            else:
                if oStockProducto.iStock < iUnidades:
                    self._registrarError(GestorErrores.ERR_ALMACEN_STOCK_INSUFICIENTE)
                    sSalida = f"No hay Stock suficiente del producto: {oStockProducto.oProducto.sNombre}"
                    sSalida += f"Stock actual: {oStockProducto.iStock}"

                elif oStockProducto.iStock > iUnidades:
                    oStockProducto.iStock -= iUnidades
                    sSalida = f"Unidades decrementadas al stock del producto: {oStockProducto.oProducto.sNombre}"

                else:
                    #Caso stock se queda a cero
                    self.lStock.remove(oStockProducto)
                    sSalida = (f"Unidades decrementadas al stock del producto: {oStockProducto.oProducto.sNombre}")
                    sSalida += (f" Ya no quedan existencias (Eliminado de stock")

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