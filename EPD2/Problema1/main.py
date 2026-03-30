from EPD2.Problema1.GestorErrores.GestorErrores import GestorErrores
from EPD2.Problema1.Modelo.Persona import Persona
from EPD2.Problema1.Modelo.Agenda import Agenda

def mostrarErrores(oObjeto):
    if len(oObjeto.getErrores()) > 0:
        print(f"ERRORES DETECTADOS en: {oObjeto}")
        for iCodigo in oObjeto.getErrores():
            print(f"  -> {GestorErrores.getMensajeError(iCodigo)}")
        oObjeto.limpiarErrores()

oP1 = Persona("Daniel","Rodriguez","666888222")
oP2 = Persona("","Dominguez","otro")

oAgenda = Agenda("Agenda.txt") # Le damos ruta fichero

oAgenda.cargarAgenda()
oAgenda.añadirEnAgenda(oP1)
mostrarErrores(oP1)
oAgenda.añadirEnAgenda(oP1)
mostrarErrores(oP1)
oAgenda.añadirEnAgenda(oP2)
mostrarErrores(oP2)
mostrarErrores(oAgenda)
Telefono = oAgenda.buscarContacto("Daniel","Rodriguez")
print(Telefono)

oAgenda.guardarAgenda()

sTelefono = oAgenda.borrarContacto("Daniel","Rodriguez")
print(f"Contacto encontrado: {sTelefono}")

print(oAgenda)
