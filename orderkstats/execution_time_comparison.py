import numpy as np
import matplotlib.pyplot as plt
from random import randint
from brute import brute_force
from order_and_select import order_and_select, quicksort
from kselect import k_select
from heap_select import heap_select
from k_heapsort import k_heapsort
from quickselect import quickselect
import timeit

TEST_LIST_SIZE = 200
NUMBER_OF_TESTS = 50


def priority_min_integers(a, b):
    if a == b:
        return 0
    elif a > b:
        return -1
    return 1


def priority_max_integers(a, b):
    return -(priority_min_integers(a, b))


def generate_list():
    l = []
    for i in range(TEST_LIST_SIZE):
        rand = randint(0, 100)
        if rand not in l:
            l.append(randint(0, 50))
        else:
            l.append(l[i-1] + 50)
    return l

n = 6
means = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(NUMBER_OF_TESTS):
    l = generate_list()
    index = randint(0, NUMBER_OF_TESTS-1)
    start_time = timeit.default_timer()
    brute_force(l, index)
    means[0] += timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    order_and_select(l, quicksort, index)
    means[1] += timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    k_select(l, index)
    means[2] += timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    k_heapsort(priority_min_integers, l, index + 1)
    means[3] += timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    heap_select(priority_max_integers, priority_min_integers, l, index + 1)
    means[4] += timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    quickselect(l, index)
    means[5] += timeit.default_timer() - start_time


for j in range(len(means)):
    means[j] *= 1000000  # Micro Secs
    means[j] /= NUMBER_OF_TESTS

index = np.arange(n)
bar_width = 0.7

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects = plt.bar(index, means, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config)

plt.xlabel('Algorithm')
plt.ylabel('Time (micro sec)')
plt.title('Execution time by algorithm')
labels = ('Brute', 'Order & Select', 'K Select', 'K Heapsort', 'Heapselect', 'Quickselect')
plt.xticks(index + bar_width/2, labels)
plt.legend()

plt.tight_layout()
plt.show()
