def verifyNumber (text=None):
    auth = False
    while not auth:
        number = input(f'{text}')
        if number.isdigit() and (int(number) % 1 == 0):
            auth = True
        else:
            print(f'Intente de nuevo')
    return int(number)

def verifySelection ():
    auth = False

    while not auth:
        selection = input('Seleccione una opcion: ')
        print('')
        if selection.isdigit() and int(selection) > 0 and int(selection) < 5:
            auth = True
        else:
            print(f'Intente de nuevo')
    return int(selection)