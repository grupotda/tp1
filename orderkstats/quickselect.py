def select(array, left, right, k):
    # Place pivot in correct position
    wall = left
    for i in range(left, right):
        if array[i] < array[right]:
            array[wall], array[i] = array[i], array[wall]
            wall += 1
    array[wall], array[right] = array[right], array[wall]
    # Return k or keep selecting
    keep_selecting = wall - k
    if not keep_selecting:
        return array[wall]
    elif keep_selecting < 0:
        return select(array, wall + 1, right, k)
    else:
        return select(array, left, wall - 1, k)

def quickselect(array, k):
    return select(array, 0, len(array)-1, k)


