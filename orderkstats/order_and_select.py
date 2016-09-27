def partition(l,pos_i,pos_f):
    pivot = l[pos_f] 
    j = pos_i
    for i in range(pos_i,pos_f):
        if l[i] <= pivot:
            '''Swap el primero de todos los mayores con este'''
            l[i],l[j] = l[j],l[i]
            j += 1
    '''Swap el pivote que quedo al final con el primero de todos los mayores'''
    l[j],l[pos_f] = l[pos_f],l[j]
    return j

def quicksort(l,pos_i,pos_f):
    if pos_i < pos_f:
        j = partition(l,pos_i,pos_f)
        quicksort(l,pos_i,j-1)
        quicksort(l,j+1,pos_f)


def select_kth(l,sort,pos_i,pos_f,k):
    sort(l,pos_i,pos_f)
    return l[k]

import random
l = range(100)
random.shuffle(l)
l = l[:16]
quicksort(l,0,len(l)-1)
print l
for k in range(len(l)):
    print k,",",select_kth(l,quicksort,0,len(l)-1,k)
