#!/usr/bin/python
#  -*- coding: utf-8 -*-
from path import Path
from heapq import heappop, heappush, heapify
from digraph import Digraph, Edge


class Dijkstra(Path):
    """
    Algoritmo de Dijkstra
    """
    def _algorithm(self):
        # heap inicializado con vertice origen
        heap = [(0, self.src)]
        for v in self.graph:
            self.distances[v] = float("inf")
	self.distances[self.src] = 0
        while heap and not self.tagged[self.dst]:
			d, v = heappop(heap)
                        self.tagged[v] = True
			for e in self.graph.adj_e(v):
				newDistance = self._priority(e)
				if not self.tagged[e.dst] and (newDistance < self.distances[e.dst]):
					self.distances[e.dst] = newDistance
					self.edge_to[e.dst] = e
                                        heappush(heap,(newDistance,e.dst))
                                        

		

    def _priority(self, edge):
        """
        Calcula la prioridad de esa arista.
        :param edge: Arista a agregar al heap, Edge.dst no fue visitado, Edge.src si
        :return: un objeto comparable. Menor implica ser de mayor prioridad.
        """
        return self.distances[edge.src] + edge.weight
