def select_min_and_swap_with_first(l):
    min = l[0]
    n = 0
    for i in range(1,len(l)):
        if l[i] < min:
            min = l[i]
            n = i
    l[n] = l[0]
    l[0] = min
    return l

def k_select(l,k):
    new_l = select_min_and_swap_with_first(l)
    if k == 0:
        return new_l[0]
    return k_select(l[1:],k-1)

import random

l = range(1,100)
random.shuffle(l)
l = l[:16]
print l
for k in range(len(l)):
        print k,",",k_select(l,k)
