tupla_vacia = ()

# Agregar , al final cuando es de un solo elemento
tupla_un_elemento = (40,)
no_tupla = (40)

print(type(tupla_un_elemento))
print(type(no_tupla))

tupla_mixta = (40, 50, 60 , 'a', 'b')

print(tupla_mixta)

# Leer

print(tupla_mixta[4])

# Longitud de la tupla

print(len(tupla_mixta))

tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = tupla1 + tupla2

tupla3 = tupla3 + (7,)

print(tupla3)