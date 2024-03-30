lista = [2, 1, 3, 5, 4]
print('> Lista desordenada: ', lista)

def particion(lista):
    pivote = lista[0]
    menor = []
    mayor = []

    for i in range(1, len(lista)): 
        if lista[i] < pivote:
            menor.append(lista[i])
        else:
            mayor.append(lista[i])

    return menor, pivote, mayor

def quicksort(lista):
    if len(lista) < 2:
        return lista 

    menor, pivote, mayor = particion(lista)
    return quicksort(menor) + [pivote] + quicksort(mayor)

print('> Lista ordenada:', quicksort(lista))

def busquedaBin(lista, buscar):
    '''
        > Funcion para aplicar la busqueda Binaria
    '''

    inicio = 0 # El inicio va a ser el primer elemento de la lista ordenada
    final = len(lista) - 1 # el final va a ser la cantidad de elementos de la lista - 1, porq el 0 cuenta

    while inicio <= final:
        medio = (inicio + final) // 2 # la mitad de la lista
        if lista[medio] == buscar: # si el elemento del medio es lo mismo que el elemento que buscamos: 
            return True
        elif lista[medio] < buscar: # si el elemento del medio es menor que el elemento que buscamos: 
            inicio = medio + 1 
        elif lista[medio] > buscar: # si el elemento del medio es mayor que el elemento que buscamos: 
            final = medio - 1
    return False

buscar = int(input('> Ingresa un numero que deseas buscar en la lista: '))
if busquedaBin(lista, buscar):
    print('> Encontre el numero! ')
else:
    print('> No encontre nada')
