conjunto0 = {1,2,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3}

print(conjunto0)

conjunto1 = {1,2,3,4}
conjunto2 = {3,4,5,6}

print("conjunto 1 y 2:")
print(conjunto1)
print(conjunto2)

print("union:")
print(conjunto1.union(conjunto2))

print("intersection:")
print(conjunto1.intersection(conjunto2))

print("difference:")
print(conjunto1.difference(conjunto2))

print("symmetric_difference:")
print(conjunto1.symmetric_difference(conjunto2))

# Agregar un elemento

conjunto0.add(6)
print(conjunto0)

# Extraer el primer elemento del conjunto
print(conjunto0.pop())