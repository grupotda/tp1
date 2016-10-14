from heap import Heap


def heap_select(heap_comparison, comparison_function, array, k):

    length = len(array)
    heap = Heap(heap_comparison, array[0:k + 1])  # heapify de los 1eros k elementos
        
    for x in range(k + 1, length):
        element = heap.view_first()
        current = array[x]
        
        if comparison_function(element, current) <= -1:  # Current es mas chico que el elemento mas grande, lo encolo
            heap.dequeue()
            heap.enqueue(current)

    return heap.view_first()
