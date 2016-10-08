#!/usr/bin/python
#  -*- coding: utf-8 -*-
from digraph import Digraph, Edge
from bfs import Bfs
from dijkstra import Dijkstra
from heuristicsearch import HeuristicSearch
from a_star import AStar

# informacion de posicion de vertices
# Para la heuristica y para posicion fija en el dibujo
vertices = [
    (0, 0),
    (1, 0),
    (-1, -1),
    (0, 1),
    (1, 2),
    (0, 2),
    (-1, 2)
]

ORIGEN = 0
DESTINO = 6

aristas = [
    (0, 2, 10),
    (0, 1, 20),
    (0, 3, 2),
    (4, 3, 3),
    (3, 5, 5),
    (5, 6, 1)
]

# llamada estandar de (grafo, src, dst)
algoritmos = [
    Bfs,
    Dijkstra
    #HeuristicSearch
    #AStar
]

nombres_alg = [
    "BFS",
    "Dijkstra"
]

COLOR_CAMINO = "\"green3\""
COLOR_NO_CAMINO = "\"red3\""
NOMBRE_ARCH_SUFIJO = "grafo1.txt"

assert 0 <= ORIGEN < len(vertices)
assert 0 <= DESTINO < len(vertices)

g = Digraph(len(vertices))

for src, dst, weight in aristas:
    g.add_edge(src, dst, weight)

paths = [alg(g, ORIGEN, DESTINO) for alg in algoritmos]


for j in xrange(len(paths)):
    #Generar la informacion para archivo de graphviz
    alg = paths[j]
    node_atts = [{} for x in xrange(g.V())]
    edge_atts = {}
    for i in xrange(g.V()):
        x, y = vertices[i]
        node_atts[i]["pos"] = "\"%d,%d!\"" % (x, y)
        if alg.visited(i):
            node_atts[i]["color"] = COLOR_NO_CAMINO
            for e in alg.path(i):
                tuple_edge = (e.src, e.dst, e.weight)
                if edge_atts.has_key(tuple_edge):
                    edge_atts[tuple_edge]["color"] = COLOR_NO_CAMINO
                else:
                    edge_atts[tuple_edge] = {"color":COLOR_NO_CAMINO}

    node_atts[ORIGEN]["label"] = "\"SRC\""
    node_atts[DESTINO]["label"] = "\"DST\""
    node_atts[DESTINO]["color"] = COLOR_CAMINO
    for e in alg.path(DESTINO):
        tuple_edge = (e.src, e.dst, e.weight)
        node_atts[e.src]["color"] = COLOR_CAMINO
        if edge_atts.has_key(tuple_edge):
            edge_atts[tuple_edge]["color"] = COLOR_CAMINO
        else:
            edge_atts[tuple_edge] = {"color": COLOR_CAMINO}

    #Escribimos el archivo
    nombre_salida = nombres_alg[j]+"_"+NOMBRE_ARCH_SUFIJO
    with open(nombre_salida, "w") as salida:
        salida.write("Digraph G {\n")
        salida.write("\toverlap = scale;\n")
        salida.write("\tsplines = true;\n")
        salida.write("\tlabelloc = \"t\"")
        salida.write("\tlabel = \"%s\"" % nombres_alg[j])
        for i in xrange(g.V()):
            atts = "["+reduce(lambda a,b: a+" "+b, [k+"="+v for k,v in node_atts[i].items()]) + "]"
            salida.write("\t%d %s\n" % (i, atts))

        for edge in aristas:
            if edge_atts.has_key(edge):
                edge_atts[edge]["label"] = "\"%d\"" % edge[2]
            else:
                edge_atts[edge] = {"label": "\"%d\"" % edge[2]}
            atts = "[" + reduce(lambda a, b: a + " " + b, [k+"="+v for k,v in edge_atts[edge].items()]) + "]"
            salida.write("\t%s -> %s %s\n" % (edge[0], edge[1], atts))
        salida.write("}\n")
