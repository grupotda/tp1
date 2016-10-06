def check_solution(array, k, x):
    '''Chequea si el valor x es el k-esimo elemento mas chico del array'''
    count = 0
    for i in range(len(array)):
        if array[i] < x:
            count += 1
    return count == k

def brute_force(array, k):
    '''Devuelve el est. de orden k del array'''
    for i in range(len(array)):
        if check_solution(array, k, array[i]):
            return array[i]