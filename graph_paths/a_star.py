#!/usr/bin/python
#  -*- coding: utf-8 -*-
from heuristicsearch import HeuristicSearch
from dijkstra import Dijkstra


class AStar(HeuristicSearch):
    """
    A* es una extension del algoritmo de Dijkstra.
    Recibe ayuda de una funcion de heuristica para guiar la busqueda.
    """

    def _priority(self, edge):
        """
        Ver HeuristicSearch / Dijkstra.
        """
        return Dijkstra._priority(self, edge) + super(AStar, self)._priority(edge)