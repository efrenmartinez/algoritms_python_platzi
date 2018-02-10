# -*- coding:utf-8 -*-


def say_hello():
    try:
        age = int(input('Cuál es tu edad '))

        if age > 18:
            print('mayor de edad')
        else:
            print('menor de edad')
    except ValueError:
        print('No recibe caracteres.')



if __name__ == '__main__':
    say_hello()
