def check_solution(l,k,x):
    count = 0
    for i in range(len(l)):
        if l[i] < x:
            count += 1
    return count == k

def brute_force(l,k):
    for i in range(len(l)):
        if check_solution(l,k,l[i]):
            return l[i]

import random

l = range(1,100)
random.shuffle(l)
l = l[:16]
print l
for k in range(len(l)):
    print k,",",brute_force(l,k)

