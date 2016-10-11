#!/usr/bin/python
# -*- coding: utf-8 -*-


def division_techo(dividendo, divisor):

    return (dividendo + divisor / 2) / divisor


def swap(array, p1, p2):
    '''Intercambia los valores de la posicion 'p1' con 'p2' de la lista
       'array' '''

    aux = array[p1]
    array[p1] = array[p2]
    array[p2] = aux


class Heap(object):

    def __init__(self, funcion_comparacion, Array=[]):

        self.datos = list(Array)
        self.cantidad_elementos = len(self.datos)
        self.comparar_prioridad = funcion_comparacion
        self.index = {}
        for i in range(len(self.datos)):
            self.index[self.datos[i][1]] = i
        self._heapify()

    def swap(self,array,p1,p2):
        aux = array[p1]
        array[p1] = array[p2]
        array[p2] = aux
        self.index[array[p1][1]] = p1
        self.index[array[p2][1]] = p2

    def empty(self):

        return not self.cantidad_elementos

    def quantity(self):

        return self.cantidad_elementos

    def view_first(self):

        maximo = 0
        try:
            return self.datos[maximo]
        except IndexError:

            return None

    def enqueue(self, elemento):

        self.datos.append(elemento)
        self.cantidad_elementos += 1
        self._upheap(self.cantidad_elementos - 1)

        return True

    def _upheap(self, pos_actual):

        if pos_actual == 0:

            return

        pos_padre = division_techo(pos_actual - 2, 2)
        dato_padre = self.datos[pos_padre]
        dato_hijo = self.datos[pos_actual]
        if self.comparar_prioridad(dato_hijo, dato_padre) > 0:

            self.swap(self.datos, pos_actual, pos_padre)
            self._upheap(pos_padre)

    def dequeue(self):

        try:

            prioritario = self.datos.pop(0)
            self.cantidad_elementos -= 1
            if len(self.datos):

                ultimo = self.datos.pop(self.cantidad_elementos - 1)
                self.datos.insert(0, ultimo)
                self._downheap(0)

            return prioritario
        except IndexError:

            return None

    def _downheap(self, posicion_actual):

        pos_h_izquierdo = 2 * posicion_actual + 1
        pos_h_derecho = 2 * posicion_actual + 2
        comparar = self.comparar_prioridad
        datos = self.datos

        if pos_h_izquierdo >= self.cantidad_elementos:  # Arbol izquierdista

            return

        pos_prioritaria = pos_h_izquierdo

        if pos_h_derecho < self.cantidad_elementos \
            and comparar(datos[pos_prioritaria], datos[pos_h_derecho]) \
            < 0 and comparar(datos[posicion_actual],
                             datos[pos_h_derecho]) < 0:

            pos_prioritaria = pos_h_derecho
        elif comparar(datos[posicion_actual], datos[pos_h_izquierdo]) \
            > 0:

                                                                           # No hay que hacer nada

            pos_prioritaria = None

        if pos_prioritaria:

            self.swap(self.datos, posicion_actual, pos_prioritaria)
            self._downheap(pos_prioritaria)

    def _heapify(self):

        inicio = self.cantidad_elementos - 1
        for pos in xrange(inicio, -1, -1):

            self._downheap(pos)

    def decreaseKey(self, k, v):
        self.datos[self.index[v]] = (k, v)
        self._downheap(self.index[v])


def heap_sort(arreglo, funcion_comparacion):

    copia_arreglo = list(arreglo)
    ultimo = len(arreglo) - 1
    heap_arr = Heap(funcion_comparacion, copia_arreglo)
    primero = 0
    while ultimo >= 0:

        prioritario = heap_arr.datos[primero]
        heap_arr.datos[primero] = heap_arr.datos[ultimo]
        heap_arr.datos[ultimo] = prioritario
        ultimo -= 1
        heap_arr.cantidad_elementos -= 1
        if ultimo < 0:
            break
        heap_arr._downheap(primero)

    return heap_arr.datos

