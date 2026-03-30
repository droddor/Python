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