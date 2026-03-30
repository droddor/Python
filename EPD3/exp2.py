from functools import reduce



def cuadrado(n,m):
    return n + m

l=[1,2,3]
l2 = reduce(cuadrado, l)

print(l2)