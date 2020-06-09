# -*- utf-8 -+-

# Aproximación

objectivo = int(input('Numero a buscar: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objectivo) >= epsilon and respuesta <= objectivo:
  respuesta += paso

if abs(respuesta**2 - objectivo) >= epsilon:
  print('No tiene raiz cuadrada.')
else:
  print(f'La raiz cuadrada de {objectivo} es {respuesta}.')