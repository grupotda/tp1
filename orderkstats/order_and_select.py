def partition(array, pos_i, pos_f):
    '''Particiona el array en dos '''
    pivot = array[pos_f]
    j = pos_i
    for i in range(pos_i, pos_f):
        if array[i] <= pivot:
            #Swap el primero de todos los mayores con este
            array[i], array[j] = array[j], array[i]
            j += 1
    #Swap el pivote que quedo al final con el primero de todos los mayores
    array[j], array[pos_f] = array[pos_f], array[j]
    return j

def quicksort(array, pos_i, pos_f):
    '''Ordena los elementos del array entre las posiciones pos_i y pos_f con quicksort'''
    if pos_i < pos_f:
        j = partition(array, pos_i, pos_f)
        quicksort(array, pos_i, j-1)
        quicksort(array, j+1, pos_f)


def select_kth(array, sort, pos_i, pos_f, k):
    '''Ordena el array luego devuelve el k elemento mas chico.'''
    ordered_array = array[:]
    sort(ordered_array, pos_i, pos_f)
    return ordered_array[k]

