
'''
Las matrices se pueden definir de dos formas:
    Un vector bidimensional que ya no posee un solo indice sino que ahora posee subindices


    Una estructura de control que almacena datos y accede a ellos mediante filas y columnas

En este tipo de estructuras de datos ya no tendremos solo una posicion del array, sino que tendremos una posicion
definida por otras 2. En Python, estas se definen como listas dentro de listas... Las listas externas son las filas de
la matriz y las listas internas son las columnas de la misma. Esto puede variar segun el criterio de cada persona.

Supongamos que tenemos una matriz A

Sintaxis:
    A= [[a, b, c],[1, 2, 3],[True, False, 24.9]]

    Aquí estamos definiendo que la matriz tendrá 3 fila y  3 columnas quedando así

    [a,     b,      c ]
    [1,     2,      3 ]
    [True, False, 24.9]

'''


def main():
    '''
    Escribir una programa que reciba dos matrices y devuelva la suma.
    '''

    '''
    [
      [1,2],
      [3,4]
    ]

    [
      [1,2],
      [3,4]
    ]
    '''

    matriz1 = [[1, 2], [3, 4]]
    matriz2 = [[1, 2], [3, 4]]
    resultado = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    print(resultado)


main()


'''
Escriba un programa que pida la cantidad de números que se tienen que escribir
 y a continuación pida números hasta que la cantidad de elementos especificada. Mostrar la cantidad de numeros
positivos, negativos, pares e impares.
'''


'''

  cantidad de numeros :  x

  ingrese el valor 1
  ingrese el valor 2
  ingrese el valor 3
  .
  .
  .

  pares : [x,x,x,x,x]
  impares : [x,x,x,x,x]
  positivos: [x,x,x,x,x]
  negativos: [x,x,x,x,x]


'''


'''
Crea un array de 10 posiciones de números aleatorios.  Muestra por consola el indice y el valor al que corresponde.
'''

'''Crea un array de números de un tamaño pasado por teclado,
el array contendrá números aleatorios impares entre los números deseados,
por último nos indica cual es el mayor de todos.'''

'''
Crea un array de números de 100 posiciones, que contendrá los números del
1 al 100. Obtén la suma de todos ellos y el promedio.

    promedio = suma(elementos)/elementos
'''

'''Realizar un programa que muestre por pantalla la traspuesta de una matriz'''
