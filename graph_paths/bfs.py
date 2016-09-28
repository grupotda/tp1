from queue import Queue
from digraph import Digraph


class Bfs:
    def __init__(self, graph, root, dst):
        self.root = root

        self.visit = []
        self.paths = {}
        self.distances = {}

        q = Queue()

        q.queue(root)
        self.distances[root] = 0
        found = False
        while q and not found:
            current = q.unqueue()
            for vertex in graph.adj(current):
                if vertex not in self.visit:
                    q.queue(vertex)
                    self.paths[vertex] = current
                    self.distances[vertex] = self.distances[current] + 1
                    self.visit.append(vertex)
                if vertex == dst:
                    found = True
                    break

    def visited(self, vertex):
        return vertex in self.visit

    def distance(self, vertex):
        """Returns distance found to vertex, or inf if vertex was not
         found"""
        if vertex not in self.distances:
            return float("inf")
        else:
            return self.distances[vertex]

    def path(self, vertex):
        """Returns list with the path found to vertex, none if there is
        no such path, or an empty list if vertex is the root"""
        if vertex == self.root:
            return []
        elif vertex not in self.visit:
            return None
        else:
            path = []
            current = vertex
            path.insert(0, current)
            while current in self.paths:
                current = self.paths[current]
                path.insert(0, current)
        return path
