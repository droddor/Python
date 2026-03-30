from EPD2.Problema1.GestorErrores.GestorErrores import GestorErrores
from EPD2.Problema1.Modelo.Persona import Persona


class Agenda:
    def __init__(self, sRutaFichero):
        self._lErrores = []
        self._lListin = []

        self._sRutaFichero = ""
        self.sRutaFichero = sRutaFichero # Para darselo mediante setter.

    # GESTION DE ERRORES
    # Metodo para registrar Error en lista
    def _registrarError(self, iCodigo):
        if iCodigo != GestorErrores.EXITO:
            self._lErrores.append(iCodigo)

    # Metodo para mostrar lista de errores
    def getErrores(self):
        return self._lErrores

    # Metodo para limpiar lista de errores
    def limpiarErrores(self):
        self._lErrores = []

    def esValido(self):
        return self._sRutaFichero != "" # Validamos que tengamos ruta de fichero

    # SETTERS / GETTERS
    @property
    def sRutaFichero(self):
        return self._sRutaFichero

    @sRutaFichero.setter
    def sRutaFichero(self, valor):
        iError = GestorErrores.EXITO
        if not isinstance(valor, str):
            iError = GestorErrores.ERR_RUTAFICHERO_TIPO
        elif len(valor) < 1:
            iError = GestorErrores.ERR_RUTAFICHERO_VACIA
        elif len(valor) > 100:
            iError = GestorErrores.ERR_RUTAFICHERO_RANGO
        else:
            self._sRutaFichero = valor
        self._registrarError(iError)

    """
    Aqui usaremos range, para ir saltando de 3 en 3, ya que son los datos que tenemos que leer. La sintaxis es esta:
    range(inicio, fin, paso)
    range(0, len(lLineas), 3)  # empieza en 0, llega al final, salta de 3 en 3
    """
    def cargarAgenda(self):
        try:
            with open(self.sRutaFichero, "r") as fichero:
                lLineas = fichero.readlines()
                # como son 3 datos de Persona, recorremos de 3 en 3 lineas
                for dato in range(0, len(lLineas),3):
                    sNombre = lLineas[dato].strip()
                    sApellido = lLineas[dato+1].strip()
                    sTelefono = lLineas[dato+2].strip()
                    oPersona = Persona(sNombre, sApellido, sTelefono)
                    if oPersona.esValido():
                        self._lListin.append(oPersona)
        except FileNotFoundError:
            pass # Si no existe, empezamos con fichero vacio


    def guardarAgenda(self):
        try:
            with open(self.sRutaFichero, "w") as fichero:
                for oPersona in self._lListin:
                    fichero.write(oPersona.sNombre + "\n")
                    fichero.write(oPersona.sApellido + "\n")
                    fichero.write(oPersona.sTelefono + "\n")
        except Exception as e:
            self._registrarError(GestorErrores.ERR_FICHERO_ESCRITURA)

    def añadirEnAgenda(self, oPersona):
        iError = GestorErrores.EXITO
        bInsertado = False
        if not isinstance(oPersona, Persona):
            iError = GestorErrores.ERR_ALTAAGENDA_TIPO
        else:
            if not oPersona.esValido():
                iError = GestorErrores.ERR_ALTAAGENDA_INVALIDO
            elif self._buscarPersona(oPersona.sNombre, oPersona.sApellido) is not None:
                bInsertado = False
            else:
                self._lListin.append(oPersona)
                bInsertado = True
        self._registrarError(iError)
        return bInsertado

    def _buscarPersona(self, sNombre, sApellido):
        oPersonaEcontrada = None
        for oPersona in self._lListin:
            if oPersona.sNombre == sNombre and oPersona.sApellido == sApellido:
                oPersonaEcontrada = oPersona
                break
        return oPersonaEcontrada

    def buscarContacto(self, sNombre, sApellido):
        oPersona = self._buscarPersona(sNombre, sApellido)
        if oPersona is not None:
            return oPersona.sTelefono
        return None


    def borrarContacto(self, sNombre,sApellido):
        bBorrado = False
        oPersona = self._buscarPersona(sNombre, sApellido)
        if oPersona is not None:
            self._lListin.remove(oPersona)
            bBorrado = True
        return bBorrado

    def mostrarErrores(oObjeto):
        if len(oObjeto.getErrores()) > 0:
            print("[!] ERRORES DETECTADOS:")
            for iCodigo in oObjeto.getErrores():
                print(f"  -> {GestorErrores.getMensajeError(iCodigo)}")
            oObjeto.limpiarErrores()

    def __str__(self):

        return f"Agenda con {len(self._lListin)} contactos cargados desde {self.sRutaFichero}"



