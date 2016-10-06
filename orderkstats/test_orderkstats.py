#!/usr/bin/python
#  -*- coding: utf-8 -*-

from k_heapsort import k_heapsort
from heap_select import heap_select
from quickselect import quickselect
from brute import brute_force
from order_and_select import order_and_select, quicksort
from kselect import k_select
import random
import pytest

def priority_min_integers(a,b):
    return -cmp(a,b)

# Uso lambdas cuando las llamadas no son estandar: (lista, k)
functions = [
    brute_force,
    lambda l, k: order_and_select(l, quicksort, k),
    k_select,
    lambda l, k: k_heapsort(priority_min_integers, l, k),
    lambda l, k: heap_select(cmp, priority_min_integers, l, k),
    quickselect,
]

function_names = [
    "brute_force",
    "order_and_select",
    "k_select",
    "k_heapsort",
    "heap_select",
    "quickselect"
]

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_unmodified_list(f):
    original = range(100, 0, -1)
    copia = list(original)
    k = len(original)/2
    f(copia, k)
    assert original == copia

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_ordered_ascending_list(f):
    l = range(100)
    k_list = range(0, len(l), 5)
    for k in k_list:
        elemento = f(l, k)
        assert elemento == l[k]

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_ordered_descending_list(f):
    l = range(100, 0, -1)
    k_list = range(0, len(l), 5)
    for k in k_list:
        elemento = f(l, k)
        assert elemento == l[len(l) - k - 1]

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_repeated_elements_in_list(f):
    l = range(5)*5
    elemento_esperado = 2
    k = len(l) / 2
    assert elemento_esperado == f(l, k)

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_negative_values_in_list(f):
    l = range(-25,25)*2
    k = 3
    elemento_esperado = -24
    assert elemento_esperado == f(l, k)

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_random_list(f):
    l = range(-25,25)*2
    sorted_l = sorted(l)
    for k in range(len(l)):
        random.shuffle(l)
        assert sorted_l[k] == f(l, k)

@pytest.mark.parametrize("f", functions, ids=function_names)
def test_big_random_list(f):
    l = range(-2000, 2000)*10 #~40000 valores
    random.shuffle(l)
    k = len(l) / 2
    elemento_esperado = 0
    assert elemento_esperado == f(l, k)