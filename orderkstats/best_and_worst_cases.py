import timeit
from brute import brute_force
from order_and_select import quicksort, order_and_select
from kselect import k_select

ARRAY_SIZE = 16
FIRST_ELEMENT = 0
LAST_ELEMENT = 15

# Brute Force
print "Brute Force"

l = range(ARRAY_SIZE)

# Peor caso: k es el ultimo elemento
start_time = timeit.default_timer()
brute_force(l, LAST_ELEMENT)
elapsed_worst = timeit.default_timer() - start_time
print "Worst case:", elapsed_worst

# Mejor caso: k es el ultimo elemento
start_time = timeit.default_timer()
brute_force(l, FIRST_ELEMENT)
elapsed_best = timeit.default_timer() - start_time
print "Best case:", elapsed_best, "\n"


# Order and Select
print "Order and Select"

# Peor caso: lista ordenada
worst = l
start_time = timeit.default_timer()
order_and_select(l, quicksort, LAST_ELEMENT)
elapsed_worst = timeit.default_timer() - start_time
print "Worst case:", elapsed_worst

# Mejor caso: el pivot termina al medio de la particion en todas las recursiones
best = [0, 1, 4, 2, 5, 7, 6, 3, 9, 11, 10, 13, 15, 14, 12, 8]
start_time = timeit.default_timer()
order_and_select(l, quicksort, FIRST_ELEMENT)
elapsed_best = timeit.default_timer() - start_time
print "Best case:", elapsed_best, "\n"


# K Select
print "K Select"

l = range(ARRAY_SIZE)

# Peor caso: k es el ultimo elemento
start_time = timeit.default_timer()
k_select(l, LAST_ELEMENT)
elapsed_worst = timeit.default_timer() - start_time
print "Worst case:", elapsed_worst

# Mejor caso: k es el ultimo elemento
start_time = timeit.default_timer()
k_select(l, FIRST_ELEMENT)
elapsed_best = timeit.default_timer() - start_time
print "Best case:", elapsed_best, "\n"


