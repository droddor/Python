"""
l = [1, 2, 3]
l2 = (n ** 2 for n in l)

[expresion    for elemento  in iterable      if condicion]
[n            for n         in range(1,100)  if n % 3 == 0]
# devuelve n  # variable    # del 1 al 99    # solo múltiplos de 3


"""


lista = [n for n in range(1,101) if n % 3 == 0]
print(lista)

