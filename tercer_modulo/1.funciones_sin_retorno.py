# Funciones
'''
Una función es un conjunto de líneas de código que realizan una tarea específica y puede retornar un valor.

Las funciones pueden tomar parámetros que modifiquen su funcionamiento.

Las funciones son utilizadas para descomponer grandes problemas en tareas simples y para implementar operaciones que
son comúnmente utilizadas durante un programa y de esta manera reducir la cantidad de código.

sintaxis:

def <nombre de la funcion> (<parametros?>):
    #cuerpo de la funcion

tipos de argumentos
- por defecto
- posicionales ✅
- nombrados ✅
- número de parámetros indefinidos 
'''


def main():

    sumatoria(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 32,
              56, 1, 23, 54, 4, 1, 43, 41, 1)
    # ejecutarOperacionAlgebraica(4, 2, "+")
    # ejecutarOperacionAlgebraica(4, 2, "-")
    # ejecutarOperacionAlgebraica(4, 2, "*")
    # ejecutarOperacionAlgebraica(4, 0, "/")

    # primerNumero = float(input("ingrese el primer numero"))
    # segundoNumero = float(input("ingrese el segundo numero"))


# args = tupla de argumentos
def sumatoria(*args):
    suma = 0

    for i in args:
        suma = suma + i

    imprimir(str(suma))


def ejecutarOperacionAlgebraica(num1: float, num2: float, operacion: str = "+"):
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
        imprimir("ERROR: Algo salió mal.")
        return

    imprimir(f"{num1} {operacion} {num2} = {resultado}")


def ejecutarSuma(num1: float, num2: float):
    suma = num1 + num2
    imprimir(f"La suma de {num1} + {num2} = {suma}")


def ejecutarResta(num1: float, num2: float):
    resta = num1 - num2
    imprimir(f"La resta de {num1} - {num2} = {resta}")


def imprimir(mensaje: str):
    print(mensaje)


main()
