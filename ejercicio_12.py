# -*- coding: utf8 -*-
def run(search_number):
    bool_option = False
    list_number = [0, 2, 4, 6, 7]
    for index in range(len(list_number)):
        if list_number[index] == search_number:
            bool_option = True
            print('El número se encuentra en índice {}'.format(search_number))
    if not bool_option:
        print('El número no se encuentra en la lista')


if __name__ == '__main__':
    try:
        search_number = int(input('Escriba el numero a buscar '))
    except ValueError: 
        print('No acepta letras.')
    run(search_number)
