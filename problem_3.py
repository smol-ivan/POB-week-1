from function import verifyNumber


def isEven (number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main ():
    number = verifyNumber('Ingrese el numero a verificar: ')
    if isEven(number) == True:
        print(f'El numero {number} es primo')
    else:
        print(f'El numero {number} no es primo')


main()