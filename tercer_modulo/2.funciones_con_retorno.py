
'''
las funciones que retornan, en otros lenguajes, se caracterizan por tener un tipo especificado en la definición.

Esto no pasaba en python. Aquí las funciones pueden retornar o no un valor, dependiendo de la situación y del contexto de
la función.

Las funciones que retornan están definidas por la clausula "return" en el cuerpo de la misma. Si se especifica al menos
 dentroreturn de la función, sí o sí, esta debe retornar algún valor.

Estas funciones devuelven un valor y, si no se almacena en una variable o estructura de datos, se perderá el valor. Por
lo tanto, debemos asegurarnos de que el valor sea inyectado en otra variable.
'''


def sayHello(name: str) -> str:

    # ... Más código ...
    return f"Hello {name}"


def rango(num: int) -> [int]:

    # numpy

    array = [0]*num
    valorAtual = 0
    for i in range(len(array)):
        array[i] = valorAtual
        valorAtual += 1

    return array


def sumaDosValores(num1: float, num2: float) -> float:

    return num1 + num2


def ejecutarOperacionAlgebraica(num1: float, num2: float, operacion: str = "+") -> float:
    resultado = 0
    if (operacion == "+"):
        resultado = num1 + num2

    elif (operacion == "-"):
        resultado = num1 - num2

    elif (operacion == "*"):
        resultado = num1 * num2

    elif (operacion == "/" and num2 != 0):
        resultado = num1 / num2

    else:
        return "ERROR: Algo salió mal."

    return f"{num1} {operacion} {num2} = {resultado}"


def main():

    suma = ejecutarOperacionAlgebraica(2, 2)

    # print(suma)

    for i in rango(5):
        print(i)


main()


''' realizar un programa que tenga las funciones basicas de una calculadora y
    que las devuelva y las imprima en consola
    

    digite el primer valor: 2
    digite el segundo valor: 2

    1. suma
    2. resta 
    3. multiplicción
    .
    .
    .

    resultado de la {operación} = {resultado}
    
'''
