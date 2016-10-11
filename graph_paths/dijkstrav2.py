#!/usr/bin/python
#  -*- coding: utf-8 -*-
from path import Path
from heap import Heap
from digraph import Digraph, Edge

def compare(a,b):
    if a[0] < b[0]:
        return 1
    if a[0] == b[0]:
        return 0
    return -1

class Dijkstra2(Path):
    """
    Algoritmo de Dijkstra
    """
    def _algorithm(self):
        # heap inicializado con vertice origen
        array = [(0, self.src)]
        for v in self.graph:
            self.distances[v] = float("inf")
            if v != self.src:
                array.append((float("inf"),v))
        heap = Heap(compare, array)
	self.distances[self.src] = 0
        while not heap.empty() and not self.tagged[self.dst]:
#                        print heap.datos
			d, v = heap.dequeue()
 #                       print "*** VISITING VERTEX ", v, " ***"
                        self.tagged[v] = True
			for e in self.graph.adj_e(v):
				newDistance = self._priority(e)
				if not self.tagged[e.dst] and (newDistance < self.distances[e.dst]):
					self.distances[e.dst] = newDistance
					self.edge_to[e.dst] = e
  #                                      print "edge ", e, " improves path to ", e.dst
                                        heap.decreaseKey(newDistance, e.dst)
   #                                     print "new heap: ", heap.datos
		

    def _priority(self, edge):
        """
        Calcula la prioridad de esa arista.
        :param edge: Arista a agregar al heap, Edge.dst no fue visitado, Edge.src si
        :return: un objeto comparable. Menor implica ser de mayor prioridad.
        """
        return self.distances[edge.src] + edge.weight
