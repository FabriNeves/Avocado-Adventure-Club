#Set

numeros = [2,2,5,8]

set_numeros = set(numeros)

print(set_numeros)

numeros2 = [2,2,3,9]

a = set(numeros)
b = set(numeros2)
print(a.symmetric_difference(b))
print(a.intersection(b))

print(a.union(b))