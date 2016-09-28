from digraph import Digraph


class Dijkstra:
    def __init__(self, graph, src, dst):
        self.graph = graph
        self.src = src
        self.dst = dst