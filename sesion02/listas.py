list_vacia = []
list_vacia2 = list()

# Lista poblada
list1 = [100,200,300,400,500]
#         0   1   2   3   4
print(list1)

# Operaciones

# Lectura (índice) --------------------------
print("list1[2]:")
print(list1[2])

# Agregar un elemento -----------------------
list1.append(600)
list1 = list1 + [700] # Concatenando

print("Después de agregar 600 y 700:")
print(list1)

# Agregar un elemento al principio ----------
list1 = [800] + list1
list1.insert(0, 900)

print("Después de agregar el 800 y 900 al principio:")
print(list1)

list1.insert(3, 150)

print("Después de agregar el 150 en la posición 2:")
print(list1)

# Leer la longitud
print("Longitud de list1:")
print(len(list1))

# Actualización de elementos
list1[3] = 1000
print("Después de actualizar la posición 3:")
print(list1)

# Eliminación de elementos
del list1[3]

print("Después de eliminar la posición 3:")
print(list1)

# Buscar el índice de un elemento
print(list1.index(500))

# Ordenar los elementos
print(sorted(list1))

list2 = ['z', 'abc', '123']

print(sorted(list2))


print([40])
print(list2.pop())