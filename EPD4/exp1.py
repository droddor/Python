"""
E1. (15 min.) Analice el siguiente cuadro de información y determine cuál es la forma de abrir un fichero según el propósito:
a) Fichero en el que se vuelca el contenido de un objeto diccionario en el que están los datos de productos de una
empresa.

with open("fichero.txt","r") as fichero:

b) Fichero de log de una aplicación, en el que se registra la actividad de una aplicación a lo largo de una sola sesión de
trabajo.


with open("fichero.txt","w") as fichero:


c) Fichero de log de una aplicación, en el que se registra la actividad de una aplicación a lo largo del tiempo.


with open("fichero.txt","a") as fichero:


d) Fichero temporal de una aplicación que se debe crear con un nombre aleatorio.

with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:


e) Fichero CSV con datos que debemos leer para insertar en una base de datos.

with open(sRutaCSV, "r", encoding="utf-8-sig") as fichero:
        oLector = csv.DictReader(fichero)
        for fila in oLector:
            tDatos = (
                fila["id"],
                fila["nombre"],
                fila["apellidos"],
                fila["puesto"],
                fila["fecha_nacimiento"],
                fila["fechaContratacion"]
            )
            cursor.execute("INSERT OR IGNORE INTO Employees VALUES (?,?,?,?,?,?)", tDatos)

    conn.commit()

f)Fichero JPG que queremos leer para aplicar un filtro a la imagen que contiene.


from PIL import Image, ImageFilter

# Abrir imagen en modo binario
with open("imagen.jpg", "rb") as f:
    oImagen = Image.open(f)

    # Aplicar filtro
    oImagenFiltrada = oImagen.filter(ImageFilter.BLUR)      # desenfoque
    oImagenFiltrada = oImagen.filter(ImageFilter.SHARPEN)   # nitidez
    oImagenFiltrada = oImagen.filter(ImageFilter.CONTOUR)   # contorno

    # Guardar resultado
    oImagenFiltrada.save("imagen_filtrada.jpg")

Se usa "rb" porque es un archivo binario

"""

