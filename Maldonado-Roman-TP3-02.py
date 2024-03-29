lista = [2, 1, 3, 5, 4]
print('> Lista desordenada: ', lista)

buscar = int(input('> Ingresa un numero que deseas buscar en la lista: '))

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

def busquedaBin (lista, buscar):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio - final) // 2
        if lista[medio] == buscar:
            print('> Encontre el numero! ')
            return True
        elif lista[medio] < buscar:
            inicio = medio + 1 
        elif lista[medio] > buscar:
            final = medio - 1
    return False

print(busquedaBin(lista, buscar))