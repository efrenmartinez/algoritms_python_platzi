# -*- coding:utf-8 -*-

def say_hello():
    age = int(raw_input('Cuál es tu edad '))

    if age > 18:
        print('mayor de edad')
    else:
        print('menor de edad')

if __name__ == '__main__':
    say_hello()
