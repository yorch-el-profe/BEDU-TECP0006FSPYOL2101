print("¿Que toping quiere?:")
print("* fresas")
print("* m&ms")
print("* oreo")
print("* brownie")

toping = input()

if toping == "fresas":
  print("El precio de tu helado es $22")
elif toping == "m&ms":
  print("El precio de tu helado es $25")
elif toping == "oreo":
  print("El precio de tu helado es $19")
elif toping == "brownie":
  print("El precio de tu helado es $28")
else:
  print("El toping no esta disponible")