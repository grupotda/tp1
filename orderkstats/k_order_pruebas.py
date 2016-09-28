from k_heapsort import k_heapsort
from heap_select import heap_select
import random

#hacer un print test
#para los de heap, obtener el k-esimo elemento mas chico mediante FB y luego comparar resultados
#alguna prueba para los demas algoritmos

def priority_min_integers(a,b):

    if a == b: return 0
    elif a > b: return -1
    return 1

def priority_max_integers(a,b):

    return -(priority_min_integers(a,b))

def test_kheapsort():

    array = range(1,100)
    random.shuffle(array)
    array = array[:14]    
    copia = list(array)
    copia.sort()
    print copia
    print array
    k_element = k_heapsort(priority_min_integers, array, 8)
    print k_element
    
test_kheapsort()

def test_heap_select():

    array = range(1,100)
    random.shuffle(array)
    array = array[:14]
    copia = list(array)
    copia.sort()
    print copia
    print array
    k_element = heap_select(priority_max_integers, priority_min_integers, array, 4)
    print k_element

test_heap_select()

#main
