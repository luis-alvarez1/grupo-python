
"""
funcion input():

    funcion utilizada para pedir datos al usuario por teclado
        (similar a un read en pseudocodigo)

    -se le puede pasar un mensaje al usuario
    -para mayor explicitud de datos, se puede encerrar en un casting (str, int, float, bool)
    -se pueden pasar variables en sus parametros
    -devuelve el dato que pasó el usuario por teclado así que este debe
        ser asignado en una variable

"""


def main():

    mensaje = "ingrese el monto: "
    cantidad = int(input("el mensaje es: " + mensaje))
    print(type(cantidad))

    ''' Realizar un programa que reciba dos datos por teclado y que devuelva la suma de ambos (+2)'''

main()
