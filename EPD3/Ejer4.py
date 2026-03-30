"""
Utilizando la función map() codifique una función que retorne una lista con la longitud de cada palabra
(separadas por espacios) de una frase. La función recibe una cadena de texto y retornara una lista.

"""
sFrase = "Hola esto es una frase"

lista = list(map(len,sFrase.split()))

print(lista)

palabras = "HOLA ESTOY EN MAYUSCULAS"

lista2 = list(map(str.lower, palabras.split()))
print(lista2)