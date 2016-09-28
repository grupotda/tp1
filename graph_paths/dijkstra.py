from digraph import Digraph


class Dijkstra:
    def __init__(self, graph, src, dst):
        self.graph = graph
        self.src = src
        self.dst = dst

        self.distances = {}
        self.visited_status = {}
        self.parents = {}
        # Set initial distances as:
        # inf for every vertex
        for vertex in graph:
            self.distances[vertex] = float("inf")
            self.visited_status[vertex] = "#unvisited"
        # except for source which is 0
        self.distances[src] = 0

        current = src
        end = False
        # Update distances to unvisited neighbours
        while not end:
            for edge in graph.adj_e(current):
                neighbour = edge.get_dst()
                if self.visited_status[neighbour] == "#unvisited":
                    new_distance = self.distances[current] + edge.get_weight()
                    if new_distance < self.distances[neighbour]:
                        self.distances[neighbour] = new_distance
                        self.parents[neighbour] = current
            self.visited_status[current] = "#visited"
            smallest_step = float("inf")
            next = None
            for neighbour in graph.adj(current):
                if self.visited_status[neighbour] == "#unvisited" and self.distances[neighbour] < smallest_step:
                    next = neighbour
                    smallest_step = self.distances[next]
            if next == dst or smallest_step == float("inf"):
                end = True
                self.visited_status[next] = "#visited"
            self.parents[next] = current
            current = next


    def visited(self, vertex):
        return self.visited_status[vertex] == "#visited"


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
        if vertex == self.src:
            return []
        elif not self.visited_status[vertex] == "#visited":
            return None
        else:
            path = []
            current = vertex
            path.insert(0, current)
            while current in self.parents:
                current = self.parents[current]
                path.insert(0, current)
        return path