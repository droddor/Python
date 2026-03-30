import csv
import os
from functools import reduce

_RUTA_P4 = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV = os.path.join(_RUTA_P4, "..", "P2", "2_air_filter.csv")

def convertirFila(dFila):
    return {
        "id": int(dFila["id"]),
        "filter_name": dFila["filter_name"],
        "location": dFila["location"],
        "filter_class": dFila["filter_class"],
        "filter_age_days": float(dFila["filter_age_days"]),
        "load_factor": float(dFila["load_factor"]),
        "pressure_drop_pa": float(dFila["pressure_drop_pa"]),
        "efficiency": float(dFila["efficiency"]),
        "inlet_pm25": float(dFila["inlet_pm25"]),
        "outlet_pm25": float(dFila["outlet_pm25"]),
        "inlet_pm10": float(dFila["inlet_pm10"]),
        "outlet_pm10": float(dFila["outlet_pm10"]),
        "replacement_needed": bool(int(dFila["replacement_needed"])),
        "hour": int(dFila["hour"])
    }

def cargarDatos(sRuta):
    with open(sRuta, "r", encoding="utf-8-sig") as csvfile:
        return list(map(convertirFila, csv.DictReader(csvfile)))

if __name__ == "__main__":

    # CARGAR DATOS
    lDatos = cargarDatos(RUTA_CSV)

    # PRUEBAS CON FILTER
    print("\n--- PRUEBAS CON FILTER ---")

    # Filtros que necesitan ser reemplazados
    lNecesitanReemplazo = list(filter(lambda f: f["replacement_needed"], lDatos))
    print(f"Filtros que necesitan ser reemplazados: {lNecesitanReemplazo}")
    print(f"Total: {len(lNecesitanReemplazo)}")

    # Filtros con eficiencia mayor a 100
    lAltaEficiencia = list(filter(lambda f: f["efficiency"] > 0.99 , lDatos))
    print(f"\nFiltros con alta eficiencia > 100.\n {lAltaEficiencia}")
    print(f"Total: {len(lAltaEficiencia)}")

    # Filtros clase HEPA con presion mayor a 100 pa
    lHepaAltaPresion = list(filter(lambda f: f["pressure_drop_pa"] > 200, lDatos))
    print(f"\nFiltros clase HEPA con presion > 200 .\n {lHepaAltaPresion}")
    print(f"Total: {len(lHepaAltaPresion)}")


    # PRUEBAS CON MAP
    print("\n--- PRUEBAS CON MAP ---")
    # Extraer solo el nombre de cada filtro
    lNombres = list(map(lambda d: d["filter_name"], lDatos))
    print(f"\nNombres de todos los filtros {lNombres[:5]}")
    print(f"Mostrados 5 - Total: {len(lNombres)}")

    # Extraer nombre y eficiencia de cada filtro
    lNombresEfic = list(map(lambda d: (d["filter_name"], d["efficiency"]), lDatos))
    print(f"\nNombre y eficiencia filtros {lNombresEfic[:5]}")
    print(f"Mostrados 5 - Total: {len(lNombresEfic)}")

    # Convertir eficiencia a porcentaje
    lEficienciaPct = list(map(lambda d: (d["filter_name"], round(d["efficiency"] * 100, 2 )), lDatos))
    print(f"\nEficiencia en porcentaje {lEficienciaPct[:5]}")
    print(f"Mostrados 5 - Total: {len(lEficienciaPct)}")

    # PRUEBAS CON REDUCE
    print("\n--- PRUEBAS CON REDUCE ---")

    iTotalReemplazo = reduce(lambda acum, d: acum + (1 if d["replacement_needed"] else 0),lDatos,0)
    print(f"\nTotal registros que necesitan reemplazo: {iTotalReemplazo}")

    # Eficiencia media global
    fSumaEfic = reduce(lambda acum, d: acum + d["efficiency"], lDatos, 0.0)
    fMediaEfic = round(fSumaEfic / len(lDatos), 4)
    print(f"\nEficiencia media global: {fMediaEfic}")


    # Registros por localizacion
    def acumularLocalizacion(dAcc, d):
        sLoc = d["location"]
        if sLoc not in dAcc:
            dAcc[sLoc] = 0
        dAcc[sLoc] += 1
        return dAcc

    dReporteLocalizacion = reduce(acumularLocalizacion, lDatos, {})
    print(f"\nRegistros por localizacion:")
    for sLoc, iTotal in sorted(dReporteLocalizacion.items(), key=lambda t: t[1], reverse=True): print(f"  {sLoc:<30} {iTotal}")


    # PRUEBA FILTER-MAP-REDUCE
    print("\n--- PRUEBA FILTER-MAP-REDUCE ---")
    filtroHEPA = lambda d: d["filter_class"] == "HEPA"
    lFiltrados = list(filter(filtroHEPA, lDatos))
    lTransformado = list(map(lambda d: (d["filter_name"], d["efficiency"]), lFiltrados))
    iTotalHepa = reduce(lambda acum, d: acum + 1, lFiltrados, 0)

    print(f"\nFiltros HEPA encontrados: {iTotalHepa}")
    print(f"Primeros 5 (nombre, eficiencia): {lTransformado[:5]}")

    # PRUEBA COMPRENSION LISTAS

    print("\n--- PRUEBA COMPRENSION LISTAS ---")
    lNombresEficAlta = [d["filter_name"] for d in lDatos if d["efficiency"] > 0.95]

    print(f"\nFiltros con eficiencia > 0.95: {len(lNombresEficAlta)}")
    print(f"Primeros 5: {lNombresEficAlta[:5]}")




