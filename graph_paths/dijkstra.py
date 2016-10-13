#!/usr/bin/python
#  -*- coding: utf-8 -*-
from path import Path
from indexed_heap import IndexedHeap


class Dijkstra(Path):
    """
    Algoritmo de Dijkstra
    """

    def _algorithm(self):
        # heap inicializado con vertice origen
        heap = IndexedHeap()
        heap._push(self.src, 0)
        self.distances[self.src] = 0
        while heap:
            v = heap.pop()
            self.tagged[v] = True

            if v == self.dst:
                break

            for e in self.graph.adj_e(v):
                if not self.tagged[e.dst]:
                    new_priority = self._priority(e)
                    if e.dst in heap:
                        if new_priority < heap[e.dst]:
                            self.distances[e.dst] = self.distances[e.src] + e.weight
                            self.edge_to[e.dst] = e
                            heap._decreaseKey(e.dst, new_priority)
                    else:
                        self.distances[e.dst] = self.distances[e.src] + e.weight
                        self.edge_to[e.dst] = e
                        heap._push(e.dst, new_priority)

    def _priority(self, edge):
        """
        Calcula la prioridad de esa arista.
        :param edge: Arista a agregar al heap, Edge.dst no fue visitado, Edge.src si
        :return: un objeto comparable. Menor implica ser de mayor prioridad.
        """
        return self.distances[edge.src] + edge.weight
