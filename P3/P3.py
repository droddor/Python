import csv
import sqlite3
from sqlite3 import Error
from tabulate import tabulate
import os

_RUTA_P3  = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV  = os.path.join(_RUTA_P3, "..", "P2", "2_air_filter.csv")
RUTA_BBDD = os.path.join(_RUTA_P3, "P3.sqlite")



# Funcion para conectar
def conectar(sRuta):
    try:
        conn = sqlite3.connect(sRuta)
        conn.row_factory = sqlite3.Row
        conn.execute('PRAGMA foreign_keys = ON')
        print("[OK] Conectado a la base de datos.")
        return conn
    except Error as e:
        print(f"[ERROR] Error al conectar a la base de datos: {e}.")
        return None


def crearTablas(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tLocalizacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        location TEXT NOT NULL UNIQUE)
                   """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tClaseFiltro (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        filter_class TEXT NOT NULL UNIQUE)
                   """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tFiltro (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        filter_name TEXT NOT NULL, 
        id_location INTEGER NOT NULL REFERENCES tLocalizacion(id), 
        id_filter_class INTEGER NOT NULL REFERENCES tClaseFiltro(id), 
        UNIQUE (filter_name, id_location))
                   """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tMedicion (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_csv INTEGER NOT NULL, 
        id_filter INTEGER NOT NULL REFERENCES tFiltro(id), 
        hour INTEGER NOT NULL, 
        filter_age_days REAL NOT NULL, 
        load_factor        REAL    NOT NULL, 
        pressure_drop_pa   REAL    NOT NULL, 
        efficiency         REAL    NOT NULL, 
        inlet_pm25         REAL    NOT NULL, 
        outlet_pm25        REAL    NOT NULL, 
        inlet_pm10         REAL    NOT NULL, 
        outlet_pm10        REAL    NOT NULL, 
        replacement_needed INTEGER NOT NULL DEFAULT 0, UNIQUE (id_csv, hour))
                   """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tAuditoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        tabla TEXT NOT NULL,
        operacion TEXT NOT NULL,
        detalle TEXT,
        fecha_hora TEXT NOT NULL DEFAULT (datetime('now', 'localtime')))
                    """)

    conn.commit()
    print("[OK] Tablas creadas.")

def crearTriggers(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TRIGGER IF NOT EXISTS medicion_insert
                       AFTER INSERT
                       ON tMedicion
                   BEGIN
                       INSERT INTO tAuditoria (tabla, operacion, detalle)
                       VALUES ('tMedicion',
                               'INSERT',
                               'Nueva medicion: id_csv=' || NEW.id_csv ||
                               ' hour=' || NEW.hour ||
                               ' efficiency=' || NEW.efficiency);
                   END
                   """)

    cursor.execute("""
                   CREATE TRIGGER IF NOT EXISTS medicion_update
                       AFTER UPDATE
                       ON tMedicion
                   BEGIN
                       INSERT INTO tAuditoria (tabla, operacion, detalle)
                       VALUES ('tMedicion',
                               'UPDATE',
                               'Medicion modificada: id_csv=' || OLD.id_csv ||
                               ' hour=' || OLD.hour ||
                               ' replacement_needed: ' || OLD.replacement_needed ||
                               '->' || NEW.replacement_needed);
                   END
                   """)
    conn.commit()
    print("[OK] Datos Auditoria creados.")

def buscarInsertar(cursor,sTabla,sCampo,sValor):
    cursor.execute(f"SELECT id FROM {sTabla} WHERE {sCampo} = ?",(sValor,))
    fila = cursor.fetchone()
    if fila:
        return fila[0]
    cursor.execute(f"INSERT INTO {sTabla} ({sCampo}) VALUES (?)",(sValor,))
    return cursor.lastrowid

def buscarInsertarFiltro(cursor, sNombreFiltro, iIdLocalizacion, iIdClase):
    cursor.execute("""
        SELECT id FROM tFiltro
        WHERE filter_name = ? AND id_location = ? 
            """,(sNombreFiltro,iIdLocalizacion))
    fila = cursor.fetchone()
    if fila:
        return fila[0]
    cursor.execute("""
        INSERT INTO tfiltro (filter_name, id_location, id_filter_class) VALUES (?,?,?)""" ,(sNombreFiltro,iIdLocalizacion,iIdClase))
    return cursor.lastrowid

def cargarCSV(conn, sRuta):
    cursor = conn.cursor()

    # Desactivar trigger INSERT durante la carga masiva del CSV
    cursor.execute("DROP TRIGGER IF EXISTS medicion_insert")

    with open(sRuta, "r", encoding="utf-8-sig") as oFichero:
        oLector = csv.DictReader(oFichero)
        for dFila in oLector:
            try:
                # Regular tabla localizacion
                iIdLocalizacion = buscarInsertar(
                    cursor, "tLocalizacion", "location", dFila["location"].strip()
                )
                # Regular tabla de filtro
                iIdClase = buscarInsertar(
                    cursor, "tClaseFiltro", "filter_class", dFila["filter_class"].strip()
                )
                # Buscar o insertar filtro
                iIdFiltro = buscarInsertarFiltro(
                    cursor,
                    dFila["filter_name"].strip(),
                    iIdLocalizacion,
                    iIdClase
                )
                # Insertar medicion

                cursor.execute("""
                               INSERT OR IGNORE INTO tMedicion
                               (id_csv, id_filter, hour, filter_age_days, load_factor,
                                pressure_drop_pa, efficiency, inlet_pm25, outlet_pm25,
                                inlet_pm10, outlet_pm10, replacement_needed)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                               """, (
                                   int(dFila["id"]),
                                   iIdFiltro,
                                   int(dFila["hour"]),
                                   float(dFila["filter_age_days"]),
                                   float(dFila["load_factor"]),
                                   float(dFila["pressure_drop_pa"]),
                                   float(dFila["efficiency"]),
                                   float(dFila["inlet_pm25"]),
                                   float(dFila["outlet_pm25"]),
                                   float(dFila["inlet_pm10"]),
                                   float(dFila["outlet_pm10"]),
                                   int(dFila["replacement_needed"])
                               ))
            except (ValueError, KeyError):
                pass

    conn.commit()

    # Reactivar auditoria despues de insertar
    cursor.execute("""
                   CREATE TRIGGER IF NOT EXISTS medicion_insert
                       AFTER INSERT
                       ON tMedicion
                   BEGIN
                       INSERT INTO tAuditoria (tabla, operacion, detalle)
                       VALUES ('tMedicion',
                               'INSERT',
                               'Nueva medicion: id_csv=' || NEW.id_csv ||
                               ' hour=' || NEW.hour ||
                               ' efficiency=' || NEW.efficiency);
                   END
                   """)
    conn.commit()
    print("[OK] CSV cargado correctamente.")



# AUDITORIA
def auditoria(conn, itail=5):
    # Metemos la consulta a modo "texto"

    qSql ="""
        SELECT id, tabla, operacion, fecha_hora, detalle
        FROM tAuditoria
        ORDER BY id DESC LIMIT ?
    """
    lResultados = conn.execute(qSql, (itail,)).fetchall()
    print(tabulate([dict(fila) for fila in lResultados], headers="keys"))

# QUERIES

# CON WITH
def consultaWith(conn):
    # 10 mediciones mas eficientes que superan la media global de eficiencia

    qSql = """
    WITH media AS (
            SELECT AVG(efficiency) AS media_eficiencia
            FROM tMedicion
        )
        SELECT
            id_csv,
            hour,
            ROUND(efficiency, 2)  AS eficiencia,
            ROUND(media.media_eficiencia, 2)   AS media_global
        FROM tMedicion, media
        WHERE efficiency > media.media_eficiencia
        ORDER BY efficiency DESC
        LIMIT 10
    """

    # 10 mediciones mas eficientes que superan la media global de eficiencia
    lResultados = conn.execute(qSql).fetchall()
    print(tabulate([dict(fila) for fila in lResultados], headers="keys"))

def consultaWith2(conn):
    # En que localizacion hay mas filtros que necesitan ser reemplazados
    qSql = """
        WITH reemplazos AS (
        SELECT id_filter, COUNT(*) AS total_reemplazos
        FROM tMedicion
        WHERE replacement_needed = 1
        GROUP BY id_filter
    )
    SELECT
        l.location,
        SUM(r.total_reemplazos) AS total_reemplazos
    FROM reemplazos r
    JOIN tFiltro       f ON r.id_filter   = f.id
    JOIN tLocalizacion l ON f.id_location = l.id
    GROUP BY l.location
    ORDER BY total_reemplazos DESC
    """

    # En que localizacion hay mas filtros que necesitan ser reemplazados
    lResultados = conn.execute(qSql).fetchall()
    print(tabulate([dict(fila) for fila in lResultados], headers="keys"))

# CON SUBQUERY
def subConsulta(conn):
    qSql ="""
        SELECT
        m.id_csv,
        f.filter_name,
        l.location,
        ROUND(m.pressure_drop_pa, 2) AS pressure_drop_pa
    FROM tMedicion m
    JOIN tFiltro      f ON m.id_filter    = f.id
    JOIN tLocalizacion l ON f.id_location = l.id
    WHERE m.pressure_drop_pa > (
        SELECT AVG(m2.pressure_drop_pa)
        FROM tMedicion m2
    )
    ORDER BY m.pressure_drop_pa DESC
    LIMIT 10
            """
    lResultados = conn.execute(qSql).fetchall()
    print(tabulate([dict(fila) for fila in lResultados], headers="keys"))

# MODFIFICACION
def modificacion(conn):
    qSql = """
    UPDATE tMedicion
    SET replacement_needed = 1
    WHERE id_filter IN (
        SELECT f.id
        FROM tFiltro f
        JOIN tClaseFiltro c ON f.id_filter_class = c.id
        WHERE c.filter_class = 'HEPA'
    )
    AND efficiency < 0.97
    AND replacement_needed = 0
    """

    cursor = conn.execute(qSql)
    conn.commit()
    print(f"[OK] {cursor.rowcount} mediciones marcadas para reemplazar.")

# CON ESTADISTICA EFICIENCIA
def qEstadistica(conn):
    qSql ="""
    SELECT 
        c.filter_class, 
        COUNT(*) AS total_mediciones,
            ROUND(AVG(m.efficiency),2) AS eficiencia_media, 
            ROUND(MIN(m.efficiency),2) AS eficiencia_min,
            ROUND(MAX(m.efficiency),2) AS eficiencia_max,
            SUM(m.replacement_needed) AS total_reemplazar
        FROM tMedicion m
            JOIN tFiltro f ON m.id_filter = f.id
            JOIN tClaseFiltro c ON f.id_filter_class = c.id
            GROUP BY c.id
                ORDER BY eficiencia_media DESC
            """
    lResultados = conn.execute(qSql).fetchall()
    print(tabulate([dict(fila) for fila in lResultados], headers="keys"))
    

if __name__ == "__main__":
    # PRUEBA CONEXION A BBDD
    print("\n--- PRUEBA CONEXION A BBDD ---")
    conn = conectar(RUTA_BBDD)

    # PRUEBA CREACION DE TABLAS
    print("\n--- PRUEBA CREACION DE TABLAS ---")
    crearTablas(conn)

    # CREAR TABLA AUDITORIA
    print("\n--- CREAR TABLA AUDITORIA ---")
    crearTriggers(conn)

    # PRUEBA CARGA DE DATOS
    print("\n--- PRUEBA CARGA DE DATOS ---")
    cursor = conn.execute("SELECT COUNT(*) AS n FROM tMedicion")
    iTotal  = cursor.fetchone()["n"]
    if iTotal == 0:
        print("Primera ejecucion: cargando CSV...")
        cargarCSV(conn, RUTA_CSV)
    else:
        print(f"La BBDD ya tiene {iTotal} registros. Se omite la carga del CSV.")

    # PRUEBA CONSULTA ESTADISTICAS EFFICIENCIA
    print("\n--- PRUEBA CONSULTA ESTADISTICAS EFFICIENCIA ---\n")
    qEstadistica(conn)

    # PRUEBA SUBCONSULTA. Mediciones presion por encima de la media global
    print("\n--- PRUEBA SUBCONSULTA ---\n")
    print("DATOS MEDICIONES DE PRESION POR ENCIMA DE MEDIA GLOBAL\n")
    subConsulta(conn)

    # PRUEBA CONSULTA WITH
    print("\n--- PRUEBA CONSULTA CON WITH ---\n")
    print("\n10 mediciones mas eficientes que superan la media global de eficiencia\n")
    consultaWith(conn)

    print("\nLocalizaciones donde hay mas filtros que necesitan ser reemplazados\n")
    consultaWith2(conn)

    # PRUEBA CONSULTA MODIFICACION
    print("\n--- PRUEBA CONSULTA MODIFICACION ---\n")
    modificacion(conn)


    # PRUEBA DATOS AUDITORIA (5 ULTIMOS REGISTROS)
    print("\n--- PRUEBA DATOS AUDITORIA (5 ULTIMOS REGISTROS) ---\n")
    auditoria(conn,itail=5)


