# -*-  coding: utf8 -*-
import random

OPTIONS = ['PIEDRA', 'PAPEL', 'TIJERA']


def random_option():
    index = random.randint(0, len(OPTIONS) - 1)
    return OPTIONS[index]


def verify_winner(option, option_pc):
    option = option.upper()

    if option == option_pc:
        print('SON IGUALES LAS OPCIONES')
    if option == 'TIJERA':
        if option_pc == 'PAPEL':
            print('GANASTE!!!')
        elif option_pc == 'PIEDRA':
            print('GANO LA COMPUTADORA!!!')
    elif option == 'PAPEL':
        if option_pc == 'PIEDRA':
            print('GANASTE!!!')
        elif option_pc == 'TIJERA':
            print('GANO LA COMPUTADORA!!!')
    elif option == 'PIEDRA':
        if option_pc == 'TIJERA':
            print('GANASTE!!!')
        elif option_pc == 'PAPEL':
            print('GANO LA COMPUTADORA')


if __name__ == '__main__':
    print ('Eliga una opción : PIEDRA, PAPEL O TIJERA')
    option = str(input('Escriba la opcion '))
    option_pc = random_option()
    print('Opción de la computadora : {}'.format(option_pc))
    verify_winner(option, option_pc)
