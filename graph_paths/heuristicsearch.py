#!/usr/bin/python
#  -*- coding: utf-8 -*-
from dijkstra import Dijkstra


class HeuristicSearch(Dijkstra):
    """
    Identico a Dijkstra pero ignora los pesos. La prioridad en la eleccion
    de un nodo se basa en una funcion de heuristica.
    """

    def __init__(self, graph, src, dst, heuristic):
        """
        :param graph: Ver Dijkstra
        :param src: Ver Dijkstra
        :param dst: Ver Dijkstra
        :param heuristic: metodo o funcion con la sig. firma:
        objeto comparable <- heuristic(vertice_del_camino, vertice_destino)
        Nota: Se recomienda un metodo ligado a un objeto, para que el objeto
        contenga informacion externa
        """
        self.h = heuristic  # Porque el algoritmo se ejecuta en __init__
        super(HeuristicSearch, self).__init__(graph, src, dst)


    def _priority(self, edge):
        """
        Ver Dijkstra
        """
        return self.h(edge.dst, self.dst)
