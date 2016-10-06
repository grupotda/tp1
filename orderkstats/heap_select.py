from heap import Heap


def heap_select(heap_comparison, comparison_function, array, k):

    heap = Heap(heap_comparison)
    length = len(array)
    limit = 0
    for i in range(len(array)):  # Agrego los primeros k elementos al heap
        if limit > k:
            break
        heap.enqueue(array[i])
        limit += 1
        
    for x in range(k + 1, length):
        element = heap.view_first()
        current = array[x]
        
        if comparison_function(element, current) <= -1:  # Current es mas chico que el elemento mas grande, lo encolo
            heap.dequeue()
            heap.enqueue(current)

    return heap.view_first()
