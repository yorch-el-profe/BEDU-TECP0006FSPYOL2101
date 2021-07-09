persona = { "nombre": "Jorge", "edad": 28, "vacunado": False }

print(persona["nombre"])

# Actualizar un valor (dada una llave)

persona["nombre"] = "Juanito"

print(persona)

# Eliminar llave-valor

del persona["vacunado"]

print(persona)

#otro = {"nombre": "Pepito", "direccion": "Calz Ermita kljasdlkjad"}
#persona.update(otro)
#print(persona)

# Agregando una nueva llave-valor

persona["otra_llave"] = "valor"
persona["fecha_nacimiento"] = "28/09/1992"

print(persona)

# Obtener todos los elementos del diccionario como tuplas
print(persona.items())
print(persona.values())
print(persona.keys())