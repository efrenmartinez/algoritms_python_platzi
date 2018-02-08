# -*- coding: utf-8 -*-

def not_repeat(sequence):
    tuple_sequence = (sequence)
    for i in tuple_sequence:
        contador = 0
        for index in tuple_sequence:
            if i == index:
                contador += 1
        if contador == 1:
            return i
        else:
            return '_'


if __name__ == '__main__':
    sequence = str(input('Ingresa una secuencia '))

    sequence_letter = not_repeat(sequence)

    if sequence_letter == '_':
        print('todas se repiten')
    else: 
        print('Esta letra se repite una sola vez : {}'.format(sequence_letter))
