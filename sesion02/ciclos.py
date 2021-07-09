# while y for

# while condicion (booleana):

print("while:")

i = 1

while i <= 10:
  print(i)
  i = i + 1

# for

print("for:")

# Repeticion de N veces
print(range(10)) # ~ [0, 1, 2, 3, ..., 9]

for j in range(10):
  print(j)

# Iterando sobre una estructura de datos
list = [10,20,30,40,50]
list2 = []

for e in list:
  list2.append(e * 2)


print(list2)

"""
  JavaScript:

  for (let i = 0; i < 10; i++) {

  }

  const lista = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19];

  for (let i of lista) {

  }
"""