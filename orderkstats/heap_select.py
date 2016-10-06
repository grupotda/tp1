from heap import Heap

def heap_select(heap_comparison, comparison_function, array, k):

    heap = Heap(heap_comparison)
    lenght = len(array)
    limit = 0
    while limit <= k: #agrego los primeros k elementos al heap

        heap.enqueue(array[i])
        limit += 1
        
    for x in range(k + 1, lenght):
        element = heap.view_first()
        current = array[x]
        
        if comparison_function(element, current) <= -1: #current es mas chico que el elemento mas grande, lo encolo

            heap.dequeue()
            heap.enqueue(current)

    return heap.view_first()
