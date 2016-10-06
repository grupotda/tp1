from time import clock

from k_heapsort import k_heapsort
from heap_select import heap_select
from quickselect import quickselect
from brute import brute_force
from order_and_select import order_and_select, quicksort
from kselect import k_select
import random

#para los de heap, obtener el k-esimo elemento mas chico mediante FB y luego comparar resultados
#alguna prueba para los demas algoritmos


def print_test(msg, bool_expression):
    '''If <bool_expression> , prints msg + '... OK',
     else, prints msg + '... ERROR' 

     PRE: msg is a string'''

    if bool_expression:

        print msg+"... OK"
        return

    print msg+"... ERROR"


def priority_min_integers(a,b):
    if a == b: return 0
    elif a > b: return -1
    return 1


def priority_max_integers(a,b):
    return -(priority_min_integers(a,b))


def test_brute(n):
    '''Tests brute_force algorithm for finding the first k'th element in an array
       n times
    '''
    
    fail = False
    while n > 0 and not fail:
        l = range(1,100)
        random.shuffle(l)
        l = l[:16]
        l2 = list(l)
        l2.sort()
        for i in range(len(l)):
            result = brute_force(l, i)
            if result is not l2[i]:
                fail = True 
                break
        n -= 1

    print_test('Brute force test', fail == False)


def test_order_and_select(n):
    '''Tests order_and_select algorithm for finding the first k'th element in an array
       n times
    '''
    
    fail = False
    while n > 0 and not fail:
        l = range(1,100)
        random.shuffle(l)
        l = l[:16]
        l2 = list(l)
        l2.sort()
        for i in range(len(l)):
            result = order_and_select(l, quicksort, i)
            if result is not l2[i]:

                fail = True 
                break

            random.shuffle(l) 
          
        n -= 1

    print_test('Order and select test', fail == False)


def test_kselect(n):
    '''Tests kselect algorithm for finding the first k'th element in an array
       n times
    '''

    fail = False
    while n > 0 and not fail:
        l = range(1,100)
        random.shuffle(l)
        l = l[:16]
        l2 = list(l)
        l2.sort()
        for i in range(len(l)):

            result = k_select(l, i)
            if result is not l2[i]:

                fail = True 
                break

            random.shuffle(l) 
          
        n -= 1

    print_test('Kselect test', fail == False)


def test_kheapselect(n):

    '''Tests kheapselect algorithm for finding the first k'th element in an array
       n times
    '''

    fail = False
    
    while n > 0 and not fail:

        l = range(1,100)
        random.shuffle(l)
        l = l[:16]
        l2 = list(l)
        l2.sort()
        
        for i in range(len(l)):

            result = heap_select(priority_max_integers, priority_min_integers, list(l), i)
  
            if result is not l2[i]:
                           
                fail = True 
                break

            random.shuffle(l) 
          
        n -= 1
        
    print_test('kheapselect test', fail == False)
    

def test_kheapsort(n):

    '''Tests kheapsort algorithm for finding the first k'th element in an array
       n times
    '''

    fail = False
    while n > 0 and not fail:

        l = range(1, 100)
        random.shuffle(l)
        l = l[:16]
        l2 = list(l)
        l2.sort()
        
        for i in rangelen(l)):

            result = k_heapsort(priority_min_integers, list(l), i)
            if result is not l2[i]:

                fail = True
                break
        
        n -= 1

    print_test('kheapsort test', fail == False)



def test_quickselect(n):
    '''Tests quickselect algorithm for finding the first k'th element in an array
       n times
    '''    

    fail = False

    while n > 0 and not fail:

        
        l = range(1,100)
        random.shuffle(l)
        l = l[:16]
        l2 = list(l)
        l2.sort()
        for i in range(1, len(l)):

            result = quickselect(list(l), i)
            if result is not l2[i]:

                fail = True
                break
        n -= 1

    print_test('quickselect test', fail == False)
    
def pruebas_tiempo(n):

    arr = range(n)
    random.shuffle(arr)
    t1 = clock()
    res = 313
    res_brute = brute_force(list(arr), res-1)
    t_brute = clock() - t1
    t2 = clock()
    res_order_select = order_and_select(list(arr), quicksort, res-1)
    t_ord_sel = clock() - t2
    t3 = clock()    
    res_kselect = k_select(list(arr), res-1)
    t_kselect = clock() - t3
    t4 = clock()
    res_kheapsort = k_heapsort(priority_min_integers, list(arr), res)
    t_kheapsort = clock() - t4
    t5 = clock()
    res_heapselect = heap_select(priority_max_integers, priority_min_integers, list(arr), res)
    t_heapselect = clock() - t5
    t6 = clock()
    res_quickselect = quickselect(list(arr), res-1)
    t_quickselect = clock() - t6

    print_test("Resultados coinciden",res_brute == res_order_select == res_kselect == res_kheapsort == res_heapselect == res_quickselect)
    print "Tiempo brute force: "+str(t_brute)+" resultado: "+str(res_brute)
    print "Tiempo order and select: "+str(t_ord_sel)+" resultado:"+str(res_order_select)
    print "Tiempo kselect: "+str(t_kselect)+" resultado:"+str(res_kselect)
    print "Tiempo kheapsort: "+str(t_kheapsort)+" resultado:"+str(res_kheapsort)
    print "Tiempo heapselect: "+str(t_heapselect)+" resultado:"+str(res_heapselect)
    print "Tiempo quickselect: "+str(t_quickselect)+" resultado:"+str(res_quickselect)

def main():
    '''Runs all tests'''
    
    test_brute(10)
    test_order_and_select(10)
    test_kselect(10)
    test_kheapselect(10) 
    test_kheapsort(10)
    test_quickselect(10)
    pruebas_tiempo(10000)

main()
