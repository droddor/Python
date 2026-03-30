import csv
import json
import os

from GestorErrores.GestorErrores import GestorErrores
from Modelo.FiltroAire import FiltroAire


class GestorFiltros:
    def __init__(self, sRutaFichero, sRutaCSV):
        # Inicializamos lista para recoger errores (GestorErrores)
        self._lErrores = []

        # Inicializamos diccionario donde se guardaran los Objetos con su clave compuesta
        self._dFiltros = {}

        # inicializamos atributos privados
        self._sRutaFichero = ""
        self._sRutaCSV = ""

        self.sRutaFichero = sRutaFichero
        self.sRutaCSV = sRutaCSV

    # Metodos Gestion de Errores
    def _registrarError(self,iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    def getErrores(self):
        return self._lErrores

    def limpiarErrores(self):
        self._lErrores = []

    def esValido(self):
        return (self._sRutaFichero !="" and self._sRutaCSV != "")


    # Getters / Setters
    @property
    def sRutaFichero(self):
        return self._sRutaFichero

    @sRutaFichero.setter
    def sRutaFichero(self,valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor,str):
            iError = GestorErrores.ERR_RUTA_FICHERO_TIPO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_RUTA_FICHERO_VACIO
        else:
            self._sRutaFichero = valor
        self._registrarError(iError)

    @property
    def sRutaCSV(self):
        return self._sRutaCSV

    @sRutaCSV.setter
    def sRutaCSV(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):
            iError = GestorErrores.ERR_RUTA_FICHERO_TIPO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_RUTA_FICHERO_VACIO
        else:
            self._sRutaCSV = valor
        self._registrarError(iError)

    # Metodos GestorFiltros

    # Metodo privado para buscar por clave
    def _buscarFiltro(self,tClave):
        return self._dFiltros.get(tClave, None)

    # Metodo para buscar Objeto Filtro
    def buscar(self,tClave):
        oFiltroAire =  self._buscarFiltro(tClave)
        if oFiltroAire is not None:
            return oFiltroAire
        return "REGISTRO NO LOCALIZADO"

    # Metodo para añadir Registro de Filtro
    def añadir(self, oFiltroAire):
        iError = GestorErrores.EXITO
        if not isinstance(oFiltroAire, FiltroAire):
            iError = GestorErrores.ERR_FILTER_TIPO
        elif not oFiltroAire.esValido():
            iError = GestorErrores.ERR_FILTER_INVALIDO
        elif self._buscarFiltro(oFiltroAire.getClave()) is not None:
            return "REGISTRO DUPLICADO"
        else:
            self._dFiltros[oFiltroAire.getClave()] = oFiltroAire
            return "OK - REGISTRADO"
        self._registrarError(iError)

    def eliminar(self, tClave):
        if self._buscarFiltro(tClave) is not None:
            del self._dFiltros[tClave]
            return "OK - ELIMINADO"
        return "REGISTRO NO LOCALIZADO"

    def buscarPorRango(self,sCampo, valor1_inicial, valor2_final):
        lResultados = []
        for oFiltro in self._dFiltros.values():
            dCampos = {
                "iId": oFiltro.iId,
                "fFilterAgeDays" : oFiltro.fFilterAgeDays,
                "fLoadFactor" : oFiltro.fLoadFactor,
                "fPreassure" : oFiltro.fPreassure,
                "fEfficiency": oFiltro.fEfficiency,
                "fInPm25" : oFiltro.fInPm25,
                "fOutPm25" : oFiltro.fOutPm25,
                "fInPm10" : oFiltro.fInPm10,
                "fOutPm10" : oFiltro.fOutPm10,
                "iHour": oFiltro.iHour,
            }
            if sCampo in dCampos:
                if valor1_inicial <= dCampos[sCampo] <= valor2_final:
                    lResultados.append(oFiltro)
        return lResultados

    # Metodos Fichero

    # Metodo para Cargar CSV
    def cargarCSV(self):
        try:
            with open(self._sRutaCSV, "r",encoding="utf-8-sig") as ficheroCSV:
                oLector = csv.DictReader(ficheroCSV)
                for fila in oLector:
                    oFiltro = FiltroAire(
                        int(fila["id"]),
                        fila["filter_name"],
                        fila["location"],
                        fila["filter_class"],
                        float(fila["filter_age_days"]),
                        float(fila["load_factor"]),
                        float(fila["pressure_drop_pa"]),
                        float(fila["efficiency"]),
                        float(fila["inlet_pm25"]),
                        float(fila["outlet_pm25"]),
                        float(fila["inlet_pm10"]),
                        float(fila["outlet_pm10"]),
                        bool(int(fila["replacement_needed"])),
                        int(fila["hour"]),
                    )
                    if oFiltro.esValido():
                        self._dFiltros[oFiltro.getClave()] = oFiltro
        except FileNotFoundError:
            pass

    # Metodo para guardar en JSON
    def guardarFichero(self):
        try:
            with open(self._sRutaFichero, "w", encoding="utf-8") as ficheroJSON:
                lDatos = [oFiltro.toDict() for oFiltro in self._dFiltros.values()]
                json.dump(lDatos, ficheroJSON, indent=4)
        except IOError as e:
            print(f"Error al crear el archivo {e}")

    def cargarFichero(self ):
        try:
            with open(self._sRutaFichero, "r", encoding="utf-8") as ficheroJSON:
                lDatos = json.load(ficheroJSON)
                for dFiltro in lDatos:
                    oFiltro = FiltroAire(
                        int(dFiltro["id"]),
                        dFiltro["filter_name"],
                        dFiltro["location"],
                        dFiltro["filter_class"],
                        float(dFiltro["filter_age_days"]),
                        float(dFiltro["load_factor"]),
                        float(dFiltro["pressure_drop_pa"]),
                        float(dFiltro["efficiency"]),
                        float(dFiltro["inlet_pm25"]),
                        float(dFiltro["outlet_pm25"]),
                        float(dFiltro["inlet_pm10"]),
                        float(dFiltro["outlet_pm10"]),
                        bool(dFiltro["replacement_needed"]),
                        int(dFiltro["hour"])
                    )
                    if oFiltro.esValido():
                        self._dFiltros[oFiltro.getClave()] = oFiltro
        except FileNotFoundError:
            pass

    def _comprobarFichero(self):
        if os.path.exists(self._sRutaFichero):
            self.cargarFichero()
        else:
            self.cargarCSV()


    def __str__(self):
        sEstado = "[OK]" if self.esValido() else "[INVALIDO]"
        return f"{sEstado} Gestor de filtros con {len(self._dFiltros)} registros cargados."
















