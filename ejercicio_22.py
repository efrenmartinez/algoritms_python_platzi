def adjacentElementsProduct(inputArray):
    numero_anterior = 0
    resultado_mayor = 0
    contador = 0
    for i in inputArray:
        numero_actual = i
        if (contador == 0):
            numero_anterior = i
        else:
            multiplicacion = numero_anterior * numero_actual
            if ( multiplicacion > resultado_mayor ):
                resultado_mayor = multiplicacion
            numero_anterior = i
        contador+=1

    return resultado_mayor

if __name__ == '__main__':
    inputArray = [-23, 4, -3, 8, -12]
    print(adjacentElementsProduct(inputArray))