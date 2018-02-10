## factorial de un número dado
# -*- coding: utf-8 -*-
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    while True:
        try:
            number = int(input('Escribe una número dado : '))
            result = factorial(number)
            print(result)
        except ValueError:
            print('No recibe caracteres.')
    