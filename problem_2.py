from function import verifyNumber


def arrInverter(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def main ():
    lengthAray = verifyNumber('Ingrese el largo del arreglo: ')
    arr = []
    for i in range(1, lengthAray + 1):
        arr.append(i)
    print(f'El arreglo {arr} invertido seria: {arrInverter(arr)}')


main()