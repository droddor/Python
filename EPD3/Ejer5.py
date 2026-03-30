"""
EJ5. (20 min) Dado el diccionario de datos de ejemplo, realice las operaciones que se piden utilizando funciones de orden
superior (filter, map, reduce), funciones lambda y comprensión de listas. Cualquier solución que utilice bucles no se
considerará válida. Se pueden dar soluciones utilizando resultados (listas, generadores, tuplas, …) auxiliares o intermedios
La clave del diccionario está compuesta por una tupla que indica el tipo de barco (ferry o mercante) y un identificador
del barco (id_barco).
• Los valores asociados dependen del tipo de barco:
- Si se trata de un ferry el valor asociado es una tupla formada por la carga en Kg y el número de pasajeros.
- Si se trata de un mercante el valor asociado es una tupla formada por la carga en Kg y la autonomía de la
embarcación en Km.
"""
from functools import reduce

diccionario = { ("ferry",1) : [ 2500 ,350 ], # [ carga, pasajeros ]
                ("mercante",2) : [ 120000, 6500 ], # [ carga, autonomía ]
                ("mercante",3) : [ 200000, 3200 ], # [ carga, pasajeros ]
                ("ferry",4) : [ 3520 , 420] , # [ carga, pasajeros ]
                }

"""
a) Escriba una función obtenerPasajeros(diccionario), que tomando como parámetro de entrada el diccionario anterior,
devuelva una tupla con los pasajeros de cada ferry.
Para el diccionario dado el resultado sería: (350, 420) """

def obtenerPasajeros(diccionario):
    f = filter(lambda item: item[0][0] == "ferry", diccionario.items())
    m = map(lambda item: item[1][1], f)

    return tuple(m)

print(obtenerPasajeros(diccionario))

"""
b) Escribir una función mayorCarga(diccionario), que tomando como parámetro de entrada el diccionario anterior,
obtenga en una lista de un único elemento el id_barco del mercante con mayor carga.
Para el diccionario dado el resultado sería: [ 3 ]"""

def mayorCarga(diccionrio):
    f = filter(lambda item: item[0][0] == "mercante", diccionario.items())
    r = reduce(lambda m1, m2: (m1 if m1[1][0] > m2[1][0] else m2), f)

    return [ r[0][1] ]

print(mayorCarga(diccionario))