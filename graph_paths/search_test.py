from digraph import Digraph
from bfs import Bfs
from dijkstra import Dijkstra
from dijkstrav2 import Dijkstra2
import timeit
import random

def genGraph(v,e):
    graph = Digraph(v)
#    for i in range(v):
#        l = range(1,e+1)
#        random.shuffle(l)
#        dest = range(v)
#        dest.remove(i)
#        for w in l:
#            graph.add_edge(i,random.choice(dest), weight = w)
    dest = range(v)
    weights = range(1,e+1)
    for x in range(e):
        graph.add_edge(random.choice(dest),random.choice(dest), weight = random.choice(weights))
    return graph
def basic_test(Class, graph):
#    print "\n"
#    print "\n"
#    print "Graph generated, starting algorithm:", Class
    start = timeit.default_timer()
    search = Class(graph, 0, graph.V()-1) # Hasta el ultimo vertice

    end = timeit.default_timer()
    i = graph.V() - 1
    p = search.path(i)
 #   print "path to ", i, " :"
    if p:
         s = 0
         for e in p:
#             print e
             s += e.weight
         print "total distance: ", s
    else:
        print "None"

#    print "total time: ", end - start
    return end-start

def compareDijkstra(v,e,t):

    print "*** v = ", v, " e = ", e, " t = ", t, " ***"
    t1 = 0.0
    t2 = 0.0
    for i in range(t):
        start = timeit.default_timer()
    	graph = genGraph(v,e)
        end = timeit.default_timer()
 #       print "Graph ready in ", end - start
    	tv1 = basic_test(Dijkstra, graph)
    	tv2 = basic_test(Dijkstra2, graph)
  #      print "v1: ", tv1, " v2: ", tv2
        t1 += tv1
        t2 += tv2
    
    print "avg v1: ", t1/t, "avg v2: ", t2/t

#compareDijkstra(100,10,10)
#compareDijkstra(100,50,10)
#compareDijkstra(1000,10,10)
#compareDijkstra(1000,50,10)
#compareDijkstra(1000,100,10)
#compareDijkstra(1000,500,10)
#compareDijkstra(10000,10,10)
#compareDijkstra(10000,50,10)
#compareDijkstra(10000,100,10)
compareDijkstra(500,250000,20)
