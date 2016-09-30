from heap import Heap

def k_heapsort(comparation_function, array, k):

    heap = Heap(comparation_function, array)
    for i in range(k):

        element = heap.dequeue()

    return element

