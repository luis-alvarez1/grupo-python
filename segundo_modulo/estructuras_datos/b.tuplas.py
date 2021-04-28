'''
Una tupla es una colección de elementos ordenada pero que no se puede modificar, es inalterable

se pueden recorrer y consultar mas no modificar

count()    Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la tupla.

 index()    Comparte el mismo método index() del tipo lista. Este método recibe un elemento como argumento, y devuelve
 el índice de su primera aparición en la tupla.

'''


def main():
    # tupla = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tupla = ('b', 'c', 'd', 'a', 'a')

    print(tupla.index('a'))


main()
