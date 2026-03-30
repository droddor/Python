import sys
import os

from EPD2.Almacen.Almacen import Almacen
from EPD2.GestorErrores import GestorErrores
from EPD2.Modelo.Electrodomestico import Electrodomestico
from EPD2.Modelo.Televisor import Televisor
from EPD2.Modelo.Lavadora import Lavadora
from EPD2.Modelo.StockProducto import StockProducto


########################
# FUNCIONES AUXILIARES #
########################

def mostrar_errores(oAlmacen):
    """
    Comprueba si el almacén tiene errores registrados.
    Si los hay, los imprime y luego limpia el registro de errores.
    """
    if not oAlmacen.esValido():
        print("   [!] SE HAN DETECTADO ERRORES INTERNOS:")
        for iCodigo in oAlmacen.getErrores():
            print(f"       -> {GestorErrores.getMensajeError(iCodigo)}")

        # Limpiamos errores para que no afecten a la siguiente prueba
        oAlmacen.limpiarErrores()
    else:
        print("   [OK] Operación registrada correctamente sin errores internos.")


######################
# BLOQUES DE PRUEBAS #
######################
def prueba_gestion_catalogo(oAlmacen, oTv1, oLav1):
    print("\n" + "=" * 40)
    print(" 1. PRUEBAS DE GESTIÓN DE CATÁLOGO")
    print("=" * 40)

    # A) Altas correctas
    print(f"Alta TV1 ({oTv1.sNombre}): {'OK' if oAlmacen.altaCatalogo(oTv1) else 'FAIL'}")
    print(f"Alta Lav1 ({oLav1.sNombre}): {'OK' if oAlmacen.altaCatalogo(oLav1) else 'FAIL'}")

    # B) Alta duplicada
    print("\n-> Prueba: Intentando alta duplicada (TV1)...")
    if not oAlmacen.altaCatalogo(oTv1):
        print("   (Lógica correcta: El sistema rechazó el duplicado)")
    mostrar_errores(oAlmacen)

    # C) Alta tipo incorrecto
    print("\n-> Prueba: Intentando alta de objeto inválido (String)...")
    if not oAlmacen.altaCatalogo("Esto no es un electrodomestico"):
        print("   (Lógica correcta: El sistema rechazó el tipo inválido)")
    mostrar_errores(oAlmacen)

    print("\n[LISTADO ACTUAL DEL CATÁLOGO]")
    print(oAlmacen.listadoCatalogo())


def prueba_entrada_stock(oAlmacen):
    print("\n" + "=" * 40)
    print(" 2. PRUEBAS DE ENTRADA DE STOCK")
    print("=" * 40)

    # A) Entrada correcta
    print("-> Entrando stock correcto (TV: 10, Lavadora: 5)...")
    print(f"   Result: {oAlmacen.entradaStock('Samsung TV 55', 10)}")
    print(f"   Result: {oAlmacen.entradaStock('Bosch Serie 6', 5)}")

    # B) Entrada de producto inexistente
    print("\n-> Prueba: Entrada de producto NO catalogado ('Nevera Fantasma')...")
    msg = oAlmacen.entradaStock("Nevera Fantasma", 5)
    print(f"   Mensaje recibido: {msg}")
    mostrar_errores(oAlmacen)

    # C) Unidades negativas
    print("\n-> Prueba: Entrada de unidades negativas (-5)...")
    msg = oAlmacen.entradaStock("Samsung TV 55", -5)
    print(f"   Mensaje recibido: {msg}")
    mostrar_errores(oAlmacen)


def prueba_salida_stock(oAlmacen):
    print("\n" + "=" * 40)
    print(" 3. PRUEBAS DE SALIDA DE STOCK")
    print("=" * 40)

    # A) Salida correcta
    print("-> Sacando 3 unidades de TV (Había 10)...")
    print(f"   Result: {oAlmacen.salidaStock('Samsung TV 55', 3)}")

    # B) Salida excesiva
    print("\n-> Prueba: Sacando más stock del existente (100 lavadoras)...")
    msg = oAlmacen.salidaStock("Bosch Serie 6", 100)
    print(f"   Mensaje recibido: {msg}")
    mostrar_errores(oAlmacen)

    # C) Salida total (Borrado)
    print("\n-> Prueba: Sacando todo el stock restante de Lavadoras (5)...")
    print(f"   Result: {oAlmacen.salidaStock('Bosch Serie 6', 5)}")


def mostrar_estadisticas_finales(oAlmacen):
    print("\n" + "=" * 40)
    print(" 4. ESTADÍSTICAS Y CIERRE")
    print("=" * 40)

    print("[LISTADO FINAL DE STOCK]")
    print(oAlmacen.listadoStock())

    print("-" * 20)
    print(f"Total Televisores: {oAlmacen.numTelevisoresStock()}")  # Esperado: 7
    print(f"Total Lavadoras:   {oAlmacen.numLavadorasStock()}")  # Esperado: 0
    print(f"Valor Total Stock: {oAlmacen.importeTotalStock():.2f}€")
    print("-" * 20)

    print("\n[ESTADO FINAL DEL OBJETO ALMACÉN]")
    print(oAlmacen)


# ==========================================
#           EJECUCIÓN PRINCIPAL
# ==========================================

if __name__ == "__main__":
    print("=================================================")
    print("       INICIANDO SUITE DE PRUEBAS AUTOMÁTICAS")
    print("=================================================")

    # 1. SETUP: Instanciación de objetos necesarios
    miAlmacen = Almacen()
    tv1 = Televisor("Samsung TV 55", 600, 55, True)
    lav1 = Lavadora("Bosch Serie 6", 450, 9)

    # 2. EJECUCIÓN: Llamada a las funciones de prueba
    # Pasamos el almacén y los objetos necesarios
    prueba_gestion_catalogo(miAlmacen, tv1, lav1)

    prueba_entrada_stock(miAlmacen)

    prueba_salida_stock(miAlmacen)

    mostrar_estadisticas_finales(miAlmacen)

    print("\n=================================================")
    print("            FIN DE LAS PRUEBAS")
    print("=================================================")