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

def solve_trips(message, algorithm, graph, trips, heuristic = None):

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
        print "Path from vertex "+str(trip[src])+" to vertex "+str(trip[dst])
        print "->".join(str(x) for x in search.vertex_path(trip[dst]))
        raw_input("\nEnter to solve next trip\n")

def basic_test2():
    '''Runs Bfs and Dijkstra algorithm from the graph basic_graph2.png

       from different origins to different destinations 
    '''
    # def estandar de path:
    heuristica = lambda g,o,d: HeuristicSearch(g, o, d, lambda u,v: 1) #ej: piensa que todo u esta a 1 de v
    print "\n***BASIC TEST 2***\n"
    edges = [(0,3,8), (0,2,2), (0,1,1), (2,5,3), (1,4,1), (3,6,9), (4,7,1), (5,7,3), (6,7,10), (7,5,1), (2,3,1), (4,6,1)]
    graph = Digraph(8)
    src = 0
    dst = 1
    wgh = 2
    for edge in edges:
        graph.add_edge(edge[src], edge[dst], edge[wgh])
    trips = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)]
    solve_trips("First run with BFS Algorithm\n", Bfs, graph, trips)
    solve_trips("Second run with Dijkstra Algorithm\n", Dijkstra, graph, trips) 
    solve_trips("Third run with stupid Heuristic Algorithm\n", heuristica, graph, trips) 

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

def manhattan_distance_test():

    '''Tests heuristic search algorithm using the manhattan distance as the heuristic
       function'''

    
    edges = [(0,1,2),(0,4,6),(0,3,1),(1,0,2),(1,4,7),(1,2,3),(2,1,3),(2,4,8),(2,5,1),
             (3,0,1),(3,4,5),(3,6,1),(4,0,6),(4,1,7),(4,2,8),(4,3,5),(4,5,9),(4,6,12),
             (4,7,11),(4,8,10),(5,4,9),(5,2,1),(5,8,1),(6,3,1),(6,4,12),(6,7,1),(7,6,1),
             (7,4,11),(7,8,1),(8,5,1),(8,4,10),(8,7,1)
            ]
    
    graph = Digraph(9)
    src = 0
    dst = 1
    wgh = 2
    for edge in edges:
        graph.add_edge(edge[src], edge[dst], edge[wgh])
    trips = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(4,0),(4,1),(4,8),(4,5)]
    solve_trips('''Heuristic test(Manhattan distance (View Heuristic Diagrama.png)''', HeuristicSearch, graph, trips, manhattan_distance)    
    solve_trips('''AStar with Manhattan distance (View Heuristic Diagrama.png)''', AStar, graph, trips, manhattan_distance)

def main():
    basic_test(Bfs)
    basic_test(Dijkstra)
    basic_test2()
    manhattan_distance_test()

main()
