# -*- utf-8 -*-

# Enumeracion exhautiva

objectivo = int(input('Numero a buscar '))
respuesta = 0

while respuesta**2 < objectivo:
  respuesta += 1

if respuesta**2 == objectivo:
  print(f'La raiz cuadrada de {objectivo} es {respuesta}.')
else:
  print('No tiene raiz cuadrada.')