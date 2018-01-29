## Calcula el promedio de temperatura dados por el usuario
# -*- coding: utf-8 -*-

def fill_list():
    temps = []
    question = True

    while question :
        temp = float(input('### Ingresa la temperatura a calcular : '))
        question = True if str(input('### Desea ingresar otra temperatura. S/N ').upper()) == 'S' else False
        temps.append(temp)

    return temps

def calcule_temps(list_temps):
    suma = 0
    for i in list_temps:
        suma += i

    return suma / len(list_temps)

if __name__ == '__main__':
    list_temps = fill_list()
    average = calcule_temps(list_temps)
    print('### El promedio de temperatura es {}'.format(average))