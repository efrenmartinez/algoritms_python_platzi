''' 
Calculo de divisas
Calcula pesos mexicanos a dolares. 
'''
# -*- coding:utf-8 -*-


def run():
    print('Calculo de divisas')
    print('')
    
    while True:
        try:
            amount = float(input('Pesos mexicanos '))
            result = float(calcule_dolars(amount))
            print('$ {}  pesos son $ {} dolares'.format(amount, result))
            exit()
        except ValueError:
            print('No acepta caracteres.')


def calcule_dolars(amount): 
    price_dolar = 18.50
    return amount * price_dolar

if __name__ == '__main__':
    run()
