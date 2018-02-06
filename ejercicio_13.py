'''Busqueda binaria'''
# -*- coding:utf8 -*-
def binary_search(numbers, number_to_search, low, high):
    if low > high:
        return False
    
    media = int( ( low + high) / 2 )

    if numbers[media] == number_to_search:
        return True
    elif numbers[media] > number_to_search:
        binary_search(numbers, number_to_search, low, media - 1)
    else:
        binary_search(numbers, number_to_search, media + 1, high)


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    number_to_search = int(input('Número a buscar '))
    result = binary_search(numbers, number_to_search, 0, len(numbers) - 1)
    if result is True:
        print('El número se encuentra en la lista.')
    else:
        print('El número NO se encuentra en la lista.')