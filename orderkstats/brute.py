def check_solution(array, k, x):
    """Chequea si el valor x es el k-esimo elemento mas chico del array"""
    less_count = 0
    equal_count = -1
    for i in range(len(array)):
        if array[i] < x:
            less_count += 1
        elif array[i] == x:
            equal_count += 1
    found = False
    for i in range(equal_count + 1):
        if less_count + i == k:
            found = True
    return found


def brute_force(array, k):
    """Devuelve el est. de orden k del array"""
    for i in range(len(array)):
        if check_solution(array, k, array[i]):
            return array[i]
