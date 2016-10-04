def select_min_and_swap_with_first(array, pos_i, pos_f):
    '''Selecciona el valor minimo del array y lo swapea con el primer elemento'''
    min_value = array[pos_i]
    pos_min = 0
    for i in range(pos_i+1, pos_f):
        if array[i] < min_value:
            min_value = array[i]
            pos_min = i
    array[pos_min] = array[pos_i]
    array[pos_i] = min_value
    return array

def k_select(array, k):
    '''Devuelve el est. de orden k del array'''
    new_array = array[:]
    for pos_i in range(k+1):
        pos_f = len(new_array)
        select_min_and_swap_with_first(new_array, pos_i, pos_f)
    return new_array[k]
