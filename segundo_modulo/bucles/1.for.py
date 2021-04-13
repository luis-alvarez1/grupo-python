'''
Se usa para iterar sobre una secuencia de elementos

for <var index> in range(<inicio iteracion>,<final iteracion-1>):
    #codigo a repetir

Se puede iterar sobre alguna lista o se puede usar la función range() para
generar un rango de valores los cuales, nuestra variable indexadora, tomará

Tambien se puede iterar sobre cadenas
'''


def main():
    """
        range(10)

        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        i 

        range ( <inicio: numero>?, <final: numero>, <incremento: numero>? )

    Escriba un programa que pida dos números enteros y escriba qué 
    números impares desde el primero hasta el segundo. (+5)



    7  /  2
    1     3 

    """

    '''
    Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz"
    instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both 
    three and five print "FizzBuzz".
    '''

    # for i in range(1, 50+1):
    #     if (i % 3 == 0 and i % 5 == 0):
    #         print("FizzBuzz")

    #     elif (i % 3 == 0):
    #         print("Fizz")

    #     elif (i % 5 == 0):
    #         print("Buzz")

    #     else:
    #         print(i)

    '''
    Write a Python program that accepts a string and calculate the number of digits and letters.
    '''

    cadena = str(input("Ingrese su cadena: "))

    counterLetras = 0
    counterNumeros = 0

    for char in cadena:

        if char.isalpha():
            counterLetras += 1

        if char.isdigit():
            counterNumeros += 1

    print("Cantidad de letras", counterLetras)
    print("Cantidad de mnumero", counterNumeros)


main()
