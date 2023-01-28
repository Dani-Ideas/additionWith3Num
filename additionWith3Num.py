"""
Este programa suma entre 3 numeros diferentes, si 2 numeros o más son iguales el resultado será cero
"""
def check_if_number():
    error = 'debes de escribir solo numeros enteros, intentalo de nuevo: '
    while True:
        try:
            number = int(input('Ingresa un numero:  '))
            break
        except:
            print (error)
    return number


def run ():
    result_addition = 0
    number1 = check_if_number()
    number2 = check_if_number()
    number3 = check_if_number()

    if number1!=number2 and number1 != number3 and number2!= number3:
        result_addition = number1 + number2 + number3
        print('El resultado es:  {}'.format(result_addition))
    else:
        print('El resultado es:  {}\n no puedes usar el mismo numero'.format(result_addition))


if __name__ == '__main__':
    run()