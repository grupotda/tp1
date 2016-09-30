from heap import Heap

def heap_select(heap_comparation, comparation_function, array, k):

    heap = Heap(heap_comparation)
    lenght = len(array)
    for i in range(k): #agrego los primeros k elementos al heap

        heap.enqueue(array[i])

    for x in range(k, lenght):
        element = heap.view_first()
        current = array[x]
        
        if comparation_function(element, current) <= -1: #current es mas chico que el elemento mas grande, lo encolo

            s = heap.dequeue()
            heap.enqueue(current)

    return heap.view_first()
