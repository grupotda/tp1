from digraph import Digraph
from bfs import Bfs
from dijkstra import Dijkstra
from heuristicsearch import HeuristicSearch
from math_vectors import norm, vector
from a_star import AStar

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

def solve_trips(message, algorithm, graph, trips, heuristic = None, show_visited = False):

    '''Runs 'Algorithm' for all trip of 'graph' in the list 'trips' 
       displaying 'message' at the start.
    '''
    print message
    src = 0
    dst = 1
    for trip in trips:
        
        if heuristic:
            search = algorithm(graph, trip[src], trip[dst], heuristic)  
        else:
            search = algorithm(graph, trip[src], trip[dst]) 

        raw_input("\nEnter to solve next trip\n")       
        print "Path from vertex "+str(trip[src])+" to vertex "+str(trip[dst])
        print "->".join(str(x) for x in search.vertex_path(trip[dst]))
        if show_visited:

            visited_count = 0
            for v in graph:

                if search.visited(v):
                    visited_count += 1
            print "Total of vertex visited to solve trip: "+str(visited_count)
           
        
def new_graph(E, v, digraph = False):
    '''Returns graph with 'v' vertices and adds
       all the edges in 'E'

       PRE: 'E' is a list of tuples (u,v,w) with u, v valid vertices 
       for the graph and w the weight of the edge connecting them.
       'v' is a natural number.

       POST: Returns a new digraph or not-directed graph.
    '''

    graph = Digraph(v)
    src = 0
    dst = 1
    wgh = 2
    for edge in E:
        graph.add_edge(edge[src], edge[dst], edge[wgh])
        if not digraph:
            graph.add_edge(edge[dst], edge[src], edge[wgh])
    return graph

def basic_test2():
    '''Runs Bfs and Dijkstra algorithm from the graph basic_graph2.png

       from different origins to different destinations 
    '''
    # def estandar de path:
    heuristica = lambda g,o,d: HeuristicSearch(g, o, d, lambda u,v: 1) #ej: piensa que todo u esta a 1 de v
    print "\n***BASIC TEST 2***\n"
    edges = [(0,3,8), (0,2,2), (0,1,1), (2,5,3), (1,4,1), (3,6,9), (4,7,1), (5,7,3), (6,7,10), (7,5,1), (2,3,1), (4,6,1)]
    graph = new_graph(edges, 8, True)
    trips = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)]
    solve_trips("First run with BFS Algorithm (basic_graph2.png)", Bfs, graph, trips)
    solve_trips("\nSecond run with Dijkstra Algorithm (basic_graph2.png)", Dijkstra, graph, trips) 
    solve_trips("\nThird run with stupid Heuristic Algorithm (basic_graph2.png)", heuristica, graph, trips) 


def manhattan_distance(v1, v2):
    '''Manhattan distance. View 'Heuristic test diagrama.png'
    '''

    points_space = {0:(1,3), 1:(2,3), 2:(3,3), 3:(1,2), 4:(2,2), 5:(3,2), 6:(1,1),
                7:(2,1), 8:(3,1)
               }
    
    p1 = points_space[v1]
    p2 = points_space[v2]
    d = vector(p1,p2) #vector director
    return norm(d)


def manhattan_distance2(v1, v2):
    '''Manhattan distance. View 'Heuristic test diagrama.png'
    '''

    points_space = {0:(1,4), 1:(2,4), 2:(3,4), 3:(4,4), 4:(1,3), 5:(2,3), 6:(3,3),
                7:(4,3), 8:(1,2),9:(2,2), 10:(3,2), 11:(4,2), 12:(1,1), 13:(2,1),
                14:(3,1), 15:(4,1) 
               }
    
    p1 = points_space[v1]
    p2 = points_space[v2]
    d = vector(p1,p2) #vector director
    return norm(d)


def manhattan_distance_test():

    '''Tests heuristic search algorithm using the manhattan distance as the heuristic
       function'''

    
    edges = [(0,1,2),(0,4,6),(0,3,1),(1,4,7),(1,2,3),(2,4,8),(2,5,1),
             (3,4,5),(3,6,1),(4,5,9),(4,6,12),(4,7,11),(4,8,10),(5,8,1),(6,7,1),(7,8,1)
            ]
    
    graph = new_graph(edges, 9)
    trips = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(4,0),(4,1),(4,8),(4,5)]
    solve_trips('''Heuristic test w/Manhattan distance (Heuristic test diagrama.png)''', HeuristicSearch, graph, trips, manhattan_distance)    
    solve_trips('''\nAStar w/Manhattan distance (Heuristic test diagrama.png)''', AStar, graph, trips, manhattan_distance)

    edges = [(0,1,5),(0,5,3),(0,4,2.9),(1,4,1),(1,5,4),(1,6,5),(1,2,8),
             (2,5,7),(2,6,5),(2,7,5),(2,3,2),(3,6,5),(3,7,1),(4,5,8),(4,9,5),(4,8,3), 
             (5,9,2),(5,6,3),(5,10,10),(6,9,5),(6,10,3),(6,11,5),(6,7,4),(7,10,5),(7,11,1),
             (8,9,4),(8,13,5),(8,12,4),(9,12,1),(9,13,1),(9,14,2),(9,10,3),(10,13,5),
             (10,14,1),(10,15,1),(10,11,2),(11,14,5),(11,15,1),(12,13,2),(13,14,7),
             (14,15,1)
            ]
    graph = new_graph(edges, 16)
    trips = [(0,15)]
    solve_trips('''Dijkstra test (Grafo del informe))''', Dijkstra, graph, trips,None,True)
    solve_trips('''Heuristic test (Grafo del informe)''', HeuristicSearch,\
                                                graph, trips, manhattan_distance2,True)    
    solve_trips('''AStar with Manhattan distance more complex (Grilla 2.png)''', AStar, graph, trips,\
                                                             manhattan_distance2,True)
def main():

    basic_test(Bfs)
    raw_input("\nEnter for next test\n")
    basic_test(Dijkstra)
    raw_input("\nEnter for next test")
    basic_test2()
    raw_input("\nEnter for next test\n")
    manhattan_distance_test()

main()
