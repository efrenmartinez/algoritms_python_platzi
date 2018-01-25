# -*- coding: utf-8 -*-
## calcula si un numero es primo o no
def run():
    number = int(raw_input('numero '))

    int_contador = is_prime(number)
    if(int_contador > 2):
        print('no es primo')
    else:
        print('ES PRIMO')

def is_prime(number):
    number_uno = number + 1
    count = 0
    for i in range(1, number_uno):
        if number % i == 0:
            count += 1
    return count
    
if __name__ == '__main__':
    run()