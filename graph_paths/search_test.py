from digraph import Digraph
from bfs import Bfs
from dijkstra import Dijkstra
import timeit
import random

def basic_test(Class):
    print Class, "test"
    graph = Digraph(7)

    for i in range(6):
        l = range(i*100000,(i+1)*100000)
        random.shuffle(l)
        for j in l:
            graph.add_edge(i,i+1, weight = j + 1)
    start = timeit.default_timer()
    search = Class(graph, 0, 6)

    end = timeit.default_timer()
    print "total time: ", end - start
    for i in range(7):
        p = search.path(i)
        print "path to ", i, " :"
        if p:
            for e in p:
                print e
        else:
            print "None"


basic_test(Bfs)
basic_test(Dijkstra)
