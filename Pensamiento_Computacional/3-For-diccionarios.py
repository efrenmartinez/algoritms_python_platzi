# -*- coding: utf-8 -*-

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

# for estudiante in estudiantes:
#   print(estudiante)

for estudiante in estudiantes.keys():
  print(estudiante)

for estudiante in estudiantes.values():
  print(estudiante)

for pais, numero_estudiantes in estudiantes.items():
  print(pais, numero_estudiantes)