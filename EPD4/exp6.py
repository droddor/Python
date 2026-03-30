import sqlite3
from tkinter.constants import INSERT

# conexion con BD

conn = sqlite3.connect("exp6.sqlite")

# Abrir instancia
cursor = conn.cursor()

# Creacion de tabla
cursor.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TXT, salary REAL)")
conn.commit() #commit a la creacion de la tabla

# # insersion de tabla
# cursor.execute("INSERT INTO employees VALUES(1,'Daniel',2500)")
# conn.commit()

# Recorrer filas
cursor.execute("SELECT id, name FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Recorrer fila a fila con fecthone
cursor.execute("SELECT id,name,salary FROM employees")
rows = cursor.fetchone()
for row in rows:
    print(row)

# usar cursos como iterador
cursor.execute("SELECT id,name,salary FROM employees")
for row in cursor:
    print(row)

cursor.execute("UPDATE employees SET salary=4500 WHERE id=?",(1,))
conn.commit()

cursor.execute("SELECT id,name,salary FROM employees")
for row in cursor:
    print(row)

# Meter 3 empleados
#Lista con tuplas
tDatos = [
    (2,"Juan,",2500),
    (3,"Pedro",2800),
    (4,"Antonio",1580)]

cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?,?,?)",tDatos)
conn.commit()

print("="*10 + "Nueva consulta de tabla" + "="*10)
cursor.execute("SELECT id,name,salary FROM employees")
for row in cursor:
    print(row)

print("Los datos se han introducido correctamente con executemany")

# Ahora vamos a sumar la columna salary
cursor.execute("SELECT sum(salary) FROM employees")
rows = cursor.fetchall()
# rows = cursor.fetchone()
print(rows)
print(f"Suma total de salarios: {rows[0][0]}")
