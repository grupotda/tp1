from k_heapsort import k_heapsort
from heap_select import heap_select
from quickselect import quickselect
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


def test_quickselect():
    """"Faltan, estas son bastante triviales"""
    print "Quickselect test"
    print "Ordered list [1,2,3,4,5,6,7]"
    l = [1, 2, 3, 4, 5, 6, 7]
    print "Element 0 is 1: ", quickselect(l, 0) == 1
    print "Element 3 is 4: ", quickselect(l, 3) == 4
    print "Element 6 is 7: ", quickselect(l, 6) == 7
    print "Unordered list [7,3,8,3,6,3,1]"
    l = [7, 3, 8, 3, 6, 3, 1]
    print "Element 0 is 1: ", quickselect(l, 0) == 1
    print "Element 3 is 3: ", quickselect(l, 3) == 3
    print "Element 6 is 8: ", quickselect(l, 6) == 8

test_heap_select()
test_quickselect()
# main
