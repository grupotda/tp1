from heap import Heap

def k_heapsort(comparation_function, array, k):
    
    heap = Heap(comparation_function, array)
    
    while k >= 0:

        element = heap.dequeue()
        k -= 1

    return element
