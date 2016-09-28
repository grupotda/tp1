from heap import *

def k_heapsort(comparation_function, array, k):

    heap = Heap(comparation_function, array)
    for i in range(k):

        element = heap.desencolar()

    return element


