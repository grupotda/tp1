from math import sqrt

def vector(p1, p2):
    '''Returns a new 2-dimensional vector that goes through 'p1'
       and 'p2', points in 2-dimensional space
        
       PRE: p1 and p2 are tuples (x,y)
       POST: Returns a tuple (x,y) which is the direction of the new vector
    '''

    x = 0
    y = 1
    return (p2[x] - p1[x], p2[y] - p1[y])

def norm(v):
    '''Returns the norm of a 2-dimensional vector

       PRE: 'v' is a tuple (x,y) which is the direction of the vector
       POST: Returns a float, the norm of 'v'
    '''

    x = 0
    y = 1
    return sqrt((v[x]**2)+(v[y]**2))

