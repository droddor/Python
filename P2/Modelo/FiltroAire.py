from GestorErrores.GestorErrores import GestorErrores

class FiltroAire:
    # Constructor (atributos filtro Csv)
    def __init__(self, iId, sFilterName, sFilterLocation, sFilterClass,
                 fFilterAgeDays, fLoadFactor, fPreassure, fEfficiency,
                 fInPm25, fOutPm25, fInPm10, fOutPm10, bReplaceNeeded,iHour):

        # Inicializamos lista para recoger Errores (GestorErrores)
        self._lErrores = []

        # Atributos privados por defectos. Modificables bajo validacion
        self._iId = 0
        self._sFilterName = ""
        self._sFilterLocation = ""
        self._sFilterClass = ""
        self._fFilterAgeDays = 0.0
        self._fLoadFactor = 0.0
        self._fPreassure = 0.0
        self._fEfficiency = 0.0
        self._fInPm25 = 0.0
        self._fOutPm25 = 0.0
        self._fInPm10 = 0.0
        self._fOutPm10 = 0.0
        self._bReplaceNeeded = False
        self._iHour = 0

        # Atributos asignados para GET/SET
        self.iId = iId
        self.sFilterName = sFilterName
        self.sFilterLocation = sFilterLocation
        self.sFilterClass = sFilterClass
        self.fFilterAgeDays = fFilterAgeDays
        self.fLoadFactor = fLoadFactor
        self.fPreassure = fPreassure
        self.fEfficiency = fEfficiency
        self.fInPm25 = fInPm25
        self.fOutPm25 = fOutPm25
        self.fInPm10 = fInPm10
        self.fOutPm10 = fOutPm10
        self.bReplaceNeeded = bReplaceNeeded
        self.iHour = iHour

    # Metodos Gestion de Errores
    def _registrarError(self, iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    def getErrores(self):
        return self._lErrores

    def limpiarErrores(self):
        self._lErrores = []

    def esValido(self):
        return (self._iId != 0 and
                self._sFilterName != "" and
                self._sFilterLocation != "" and
                self._sFilterClass != "")

    # Getters / Setters
    @property
    def iId(self):
        return self._iId

    @iId.setter
    def iId(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, int):
            iError = GestorErrores.ERR_ID_TIPO
        elif not (10000 <= valor <= 99999):
            iError = GestorErrores.ERR_ID_RANGO
        else:
            self._iId = valor
        self._registrarError(iError)

    @property
    def sFilterName(self):
        return self._sFilterName

    @sFilterName.setter
    def sFilterName(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):
            iError = GestorErrores.ERR_FILTER_NAME_TIPO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_FILTER_NAME_VACIO
        elif len(valor) > 100:
            iError = GestorErrores.ERR_FILTER_NAME_RANGO
        else:
            self._sFilterName = valor
        self._registrarError(iError)

    @property
    def sFilterLocation(self):
        return self._sFilterLocation

    @sFilterLocation.setter
    def sFilterLocation(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):
            iError = GestorErrores.ERR_FILTER_LOCATION_TIPO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_FILTER_LOCATION_VACIO
        elif len(valor) > 100:
            iError = GestorErrores.ERR_FILTER_LOCATION_RANGO
        else:
            self._sFilterLocation = valor
        self._registrarError(iError)

    @property
    def sFilterClass(self):
        return self._sFilterClass

    @sFilterClass.setter
    def sFilterClass(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):
            iError = GestorErrores.ERR_FILTER_CLASS_TIPO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_FILTER_CLASS_VACIO
        elif len(valor) > 100:
            iError = GestorErrores.ERR_FILTER_CLASS_RANGO
        else:
            self._sFilterClass = valor
        self._registrarError(iError)

    @property
    def fFilterAgeDays(self):
        return self._fFilterAgeDays

    @fFilterAgeDays.setter
    def fFilterAgeDays(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)): #Aceptado int,float
            iError =  GestorErrores.ERR_FILTER_AGE_TIPO
        else:
            self._fFilterAgeDays = valor
        self._registrarError(iError)

    @property
    def fLoadFactor(self):
        return self._fLoadFactor

    @fLoadFactor.setter
    def fLoadFactor(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_FACTOR_TIPO
        else:
            self._fLoadFactor = valor
        self._registrarError(iError)

    @property
    def fPreassure(self):
        return self._fPreassure

    @fPreassure.setter
    def fPreassure(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_PRES_TIPO
        else:
            self._fPreassure = valor
        self._registrarError(iError)

    @property
    def fEfficiency(self):
        return self._fEfficiency

    @fEfficiency.setter
    def fEfficiency(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_EFI_TIPO
        else:
            self._fEfficiency = valor
        self._registrarError(iError)

    @property
    def fInPm25(self):
        return self._fInPm25

    @fInPm25.setter
    def fInPm25(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_PM_TIPO
        else:
            self._fInPm25 = valor
        self._registrarError(iError)

    @property
    def fOutPm25(self):
        return self._fOutPm25

    @fOutPm25.setter
    def fOutPm25(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_PM_TIPO
        else:
            self._fOutPm25 = valor
        self._registrarError(iError)

    @property
    def fInPm10(self):
        return self._fInPm10

    @fInPm10.setter
    def fInPm10(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_PM_TIPO
        else:
            self._fInPm10 = valor
        self._registrarError(iError)

    @property
    def fOutPm10(self):
        return self._fOutPm10

    @fOutPm10.setter
    def fOutPm10(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, (int,float)):
            iError = GestorErrores.ERR_FILTER_PM_TIPO
        else:
            self._fOutPm10 = valor
        self._registrarError(iError)

    @property
    def bReplaceNeeded(self):
        return self._bReplaceNeeded

    @bReplaceNeeded.setter
    def bReplaceNeeded(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, bool):
            iError = GestorErrores.ERR_FILTER_REPLACE_TIPO
        else:
            self._bReplaceNeeded = valor
        self._registrarError(iError)

    @property
    def iHour(self):
        return self._iHour

    @iHour.setter
    def iHour(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, int):
            iError = GestorErrores.ERR_FILTER_HORA_TIPO
        elif not (0 <= valor <= 23):
            iError = GestorErrores.ERR_FILTER_HORA_RANGO
        else:
            self._iHour = valor
        self._registrarError(iError)

    # Metodo para devolver clave compuesta unica
    def getClave(self):
        return (self._iId, self._sFilterName, self._iHour)


    # Metodo para convertir a diccionario -> Para guardar en fichero

    def toDict(self):
        return {
            "id" : self._iId,
            "filter_name": self._sFilterName,
            "location" : self._sFilterLocation,
            "filter_class" : self._sFilterClass,
            "filter_age_days": self._fFilterAgeDays,
            "load_factor" : self._fLoadFactor,
            "pressure_drop_pa": self._fPreassure,
            "efficiency" : self._fEfficiency,
            "inlet_pm25" : self._fInPm25,
            "outlet_pm25" : self._fOutPm25,
            "inlet_pm10" : self._fInPm10,
            "outlet_pm10" : self._fOutPm10,
            "replacement_needed" : self._bReplaceNeeded,
            "hour" : self._iHour,
        }

    # Comparador Objeto FiltroAire con validez de clave compuesta
    def __eq__(self, oFiltroAire):
        if isinstance(oFiltroAire, FiltroAire):
            return self.getClave() == oFiltroAire.getClave()
        return False


    # Metodo str ("toString") para devolver atributos
    def __str__(self):
        sEstado = "[OK]" if self.esValido() else "[INVALIDO]"
        return (f"Registro: {sEstado} "
                f"ID: {self._iId} | "
                f"Nombre: {self._sFilterName} | "
                f"Ubicaion: {self._sFilterLocation} |"
                f"Clase: {self._sFilterClass} | "
                f"Edad: {self._fFilterAgeDays} | "
                f"Factor Carga: {self._fLoadFactor} | "
                f"Presion: {self._fPreassure} | "
                f"Eficiencia: {self._fEfficiency} | "
                f"InPM25: {self._fInPm25} | "
                f"OutPM25: {self._fOutPm25} | "
                f"InPm10: {self._fInPm10} | "
                f"OutPm10: {self._fOutPm10} | "
                f"Necesita Reemplazo: {self._bReplaceNeeded} | "
                f"Hora Medicion: {self._iHour}")






