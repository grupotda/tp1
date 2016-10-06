from k_heapsort import k_heapsort
from heap_select import *
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
        
        for i in range(1, len(l)):

            result = heap_select(priority_max_integers, priority_min_integers, list(l), i)
  
            if result is not l2[i - 1]:
                           
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
        
        for i in range(1, len(l)):

            result = k_heapsort(priority_min_integers, list(l), i)
            if result != l2[i - 1]:

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
            if result != l2[i]:

                fail = True
                break
        n -= 1

    print_test('quickselect test', fail == False)

def main():
    '''Runs all tests'''
    
    test_brute(10)
    test_order_and_select(10)
    test_kselect(10)
    test_kheapselect(10)
    test_kheapsort(10)
    test_quickselect(10)

main()
