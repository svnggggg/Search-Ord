lista = [2, 1, 3, 5, 4]
print('> Lista desordenada: ', lista)

def particion(lista):
    '''
        > Funcion para partir la lista, una lista con los numeros menores al pivote
        y otra con los mayores al pivote.
        > menores al pivote a menor[] y mayores al pivote a []
    '''

    pivote = lista[0]
    menor = []
    mayor = []

    for i in range(1, len(lista)): # este for itera en un rango de 1 hasta el final de la lista 
        if lista[i] < pivote:
            menor.append(lista[i])
        else:
            mayor.append(lista[i])

    return menor, pivote, mayor  # devuelve las 3 listas 


def quicksort(lista):
    '''
        > Funcion para retornar una lista, en la cual, la funcion 'quicksort'
        fue aplicada en la lista menor[] y mayor[]
    '''

    if len(lista) < 2: # Caso base, si la lista tiene 2 elementos 
        return lista 

    menor, pivote, mayor = particion(lista)
    return quicksort(menor) + [pivote] + quicksort(mayor)

print('> Lista ordenada:', quicksort(lista))
