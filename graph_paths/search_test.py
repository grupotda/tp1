from digraph import Digraph
from bfs import Bfs
from dijkstra import Dijkstra
import timeit
import random

def basic_test(Class):
    print Class, "test"
    graph = Digraph(50)

    for i in range(50):
        l = range(1,20)
        random.shuffle(l)
        dest = range(50)
        dest.remove(i)
        for w in l:
            graph.add_edge(i,random.choice(dest), weight = w)
    print "Graph generated, starting algorithm:", Class
    start = timeit.default_timer()
    search = Class(graph, 0, 49)

    end = timeit.default_timer()
    print "total time: ", end - start
    for i in range(50):
        p = search.path(i)
        print "path to ", i, " :"
        if p:
            for e in p:
                print e
        else:
            print "None"


#basic_test(Bfs)
basic_test(Dijkstra)
