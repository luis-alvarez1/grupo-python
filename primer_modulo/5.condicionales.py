"""
Python posee tres estructuras condicionales:

1-
    if(<condicion>):
        #cuerpo si la condición se cumple
2-
    if(<condicion>):
        #cuerpo si la condición se cumple
    else:
        #si la condicion no se cumple

3-
    if(<condicion>):
        #cuerpo si la condición se cumple
    elif(<otra condicion>): # else if
        #si la condicion anterior falló y se desea evaluar otra
    else:
        #si todo lo anterior falló

"""


def main():

    id_usuario = str(input("Ingrese su identificación: "))
    id_gerente = "0"
    id_super = "1"
    id_administrador = "2"

    if(id_usuario == id_gerente):
        print("usted es gerente")
    elif (id_usuario == id_super):
        print("usted es super usuario")
    elif (id_usuario == id_administrador):
        print("usted es administrador")
    else:
        print("usted no tiene permisos")

    ''' Un programa que pida dos números y que muestre cuál es mayor, cuál es menor o si son iguales (+3)'''


main()
