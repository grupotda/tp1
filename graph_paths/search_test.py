from digraph import Digraph
from bfs import Bfs


def bfs_test():
    print "BFS test"
    graph = Digraph(7)

    graph.add_edge(0, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(5, 6)
    graph.add_edge(0, 1)
    graph.add_edge(1, 3)

    bfs = Bfs(graph, 0, 6)

    # Valid path
    print "vertex 6 was visited:", bfs.visited(6)
    print "path to 6 is [0, 2, 5, 6]:", bfs.path(6) == [0, 2, 5, 6]
    print "which is of length 3:", bfs.distance(6) == 3

    # Unconnected vertex
    print "path to 4 was not visited:", not bfs.visited(4)
    print "path to 4 is None:", not bfs.path(4)
    print "distance to 4 is inf:", bfs.distance(4) == float("inf")

    # Path to root
    print "path to root is empty list:", bfs.path(0) == []


bfs_test()
