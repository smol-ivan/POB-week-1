from function import verifyNumber, verifySelection


def addition(A, B):
    return A+B


def substraction(A, B):
    return A-B


def multiplication(A, B):
    return A*B


def division(A, B):
    if B != 0:
        return A/B
    else:
        print(f'No se puede dividir por 0')


def operationSelect ():
    options = ['Suma', 'Resta', 'Multiplicacion', 'Division']
    for i in range(len(options)):
        print(f'{i + 1} ~ {options[i]}')
    print('')
    selection = verifySelection()
    return selection


def perfomOperation (A, B, selection):
    if selection == 1:
        result = addition(A, B)
        print(f'Suma de {A} y {B}')
        print('')
    elif selection == 2:
        result = substraction(A, B)
        print(f'Resta de {A} y {B}')
        print('')
    elif selection == 3:
        result = multiplication(A, B)
        print(f'Multiplicacion de {A} y {B}')
        print('')
    else:
        result = division(A,B)
        print(f'Devision de {A} y {B}')
        print('')
    return result


def main():
    print(f'~C A L C U L A D O R A~')
    number_A = verifyNumber('Ingrese el primer numero (int): ')
    number_B = verifyNumber('Ingrese el segundo numero (int): ')
    print('')
    print('~Operaciones disponibles')
    selection = operationSelect()
    print('')
    result = perfomOperation(number_A, number_B, selection)
    print(f'El resultado es el siguiente: {result}')


main()