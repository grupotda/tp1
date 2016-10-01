from digraph import Digraph
from bfs import Bfs
from dijkstra import Dijkstra


def basic_test(Class):
    print Class, "test"
    graph = Digraph(7)

    graph.add_edge(0, 2, weight=1)
    graph.add_edge(2, 3, weight=3)
    graph.add_edge(2, 5, weight=1)
    graph.add_edge(5, 6, weight=1)
    graph.add_edge(0, 1, weight=2)
    graph.add_edge(1, 3, weight=1)

    search = Class(graph, 0, 6)

    # Valid path
    print "vertex 6 was visited:", search.visited(6)
    print "path to 6 is [0, 2, 5, 6]:", search.vertex_path(6) == [0, 2, 5, 6]
    print "which is of length 3:", search.distance(6) == 3

    # Unconnected vertex
    print "path to 4 was not visited:", not search.visited(4)
    print "path to 4 is None:", not search.vertex_path(4)
    print "distance to 4 is inf:", search.distance(4) == float("inf")

    # Path to root
    print "path to root is empty list:", search.path(0) == []


basic_test(Bfs)
basic_test(Dijkstra)
