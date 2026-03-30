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