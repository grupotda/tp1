#!/usr/bin/python
#  -*- coding: utf-8 -*-
from path import Path
from heapq import heappop, heappush
from digraph import Digraph, Edge
from heap import Heap
def compare(a,b):
    if a[0] == b[0]:
        return 0
    if a[0] < b[0]:
        return 1
    return -1

class Dijkstra(Path):
    """
    Algoritmo de Dijkstra
    """

    def _algorithm(self):
        # heap inicializado con arista mentirosa
        array = [(None, Edge(self.src, self.src, weight=0))]
        heap = Heap(compare, array)
        while not heap.empty() and not self.tagged[self.dst]:
            _, edge = heap.dequeue()
            if not self.tagged[edge.dst]: #y si mejora en cuanto a peso pero no la tiene en cuenta por esto? no estoy seguro pero despues en pruebas se vera esto

                self.edge_to[edge.dst] = edge
                self.distances[edge.dst] = self.distances.get(edge.src, 0) + edge.weight
                self.tagged[edge.dst] = True

                if edge.dst == self.dst:
                    break

                for next_edge in self.graph.adj_e(edge.dst):
                    if not self.tagged[next_edge.dst]:
                        heap.enqueue((self._priority(next_edge),next_edge))

        self.edge_to.pop(self.src)  # borro la arista mentirosa

    def _priority(self, edge):
        """
        Calcula la prioridad de esa arista.
        :param edge: Arista a agregar al heap, Edge.dst no fue visitado, Edge.src si
        :return: un objeto comparable. Menor implica ser de mayor prioridad.
        """
        return self.distances[edge.src] + edge.weight
