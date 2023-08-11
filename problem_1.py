from function import verifyNumber


def evenSum (n, m):
    if n % 2 != 0:
        n += 1
    if m % 2 != 0:
        m -= 1
    acum = 0
    while n <= m:
        acum =+ n
        n += 2
    return acum


def main ():
    n = verifyNumber('Ingrese un numero entero: ')
    m = verifyNumber('Ingrese un numero entero: ')
    print(f'La suma acumulada de numeros pares es de {evenSum(n, m)}')

main()