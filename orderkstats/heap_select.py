from heap import *

def heap_select(heap_comparation, comparation_function, array, k):

    heap = Heap(heap_comparation)
    lenght = len(array)
    for i in range(k): #agrego los primeros k elementos al heap

        heap.encolar(array[i])

    for x in range(k, lenght):
        element = heap.ver_max()
        current = array[x]
        
        if comparation_function(element, current) <= -1: #current es mas chico que el elemento mas grande, lo encolo

            s = heap.desencolar()
            heap.encolar(current)

    return heap.ver_max()
