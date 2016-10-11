#!/usr/bin/python
#  -*- coding: utf-8 -*-
from dijkstra import Dijkstra

class HeuristicSearch(Dijkstra):
    """
    Identico a Dijkstra pero ignora los pesos. La prioridad en la eleccion
    de un nodo se basa en una funcion de heuristica.
    """

    def _priority(self, edge):
        """
        Ver Dijkstra
        """
        # return self.h(graph, self.src, self.dst, edge) NO DEBERIA SER NECESARIO
        return self.h(edge.dst, self.dst)
