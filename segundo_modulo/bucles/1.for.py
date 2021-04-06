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

        0, 1, 2, 3, 4, 5, 6, 7, 8, 9 

        range ( <inicio: numero>?, <final: numero>, <incremento: numero>? ) 

    Escriba un programa que pida dos números enteros y escriba qué 
    números impares desde el primero hasta el segundo. (+5)



    7  /  2
    1     3 

    """

    num1 = int(input("ingrese el primero: "))
    num2 = int(input("ingrese el segundo: "))

    for i in range(num1, num2+1):
        if i % 2 != 0:
            print(i)


main()
