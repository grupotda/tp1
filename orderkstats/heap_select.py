from heap import Heap


def heap_select(heap_comparison, comparison_function, array, k):

    heap = Heap(heap_comparison)
    length = len(array)
    for i in range(k+1):  # Agrego los primeros k elementos al heap; + 1 porque k >= 0
        heap.enqueue(array[i])
        
    for x in range(k + 1, length):
        element = heap.view_first()
        current = array[x]
        
        if comparison_function(element, current) <= -1:  # Current es mas chico que el elemento mas grande, lo encolo
            heap.dequeue()
            heap.enqueue(current)

    return heap.view_first()
