import networkx as nx
from CertifyingAlgo.CDCLSolver import CDCLSolver
from CertifyingAlgo.NkColor import colorNktoClause

# Donne le format utilisé par les différents codes pour les arêtes
def toEdges(vertex, edges):
    tab = [[0 for _ in range(vertex)] for _ in range(vertex)]
    for tuple in edges:
        tab[tuple[0]][tuple[1]] = 1
        tab[tuple[1]][tuple[0]] = 1
    return tab

g = nx.from_graph6_bytes(b"F?B@w")

N = 3
vertex = len(g.nodes())
edge = toEdges(vertex, g.edges())

clause = colorNktoClause(edge, vertex, N)

solver = CDCLSolver(clause)
sat, model = solver.solve()

if(sat):
    print(" Le probleme est resolvable" )
else:
    print(" Le probleme n'est pas resolvable" )

print("Assignation possible :", model)

print("Signification :")

i = 1
for x in range(vertex):
    for y in range(N):
        if(model[i] == True):
            print("Le sommet " + str(x) + " a la couleur " + str(y+1) + " attribuee")
        i += 1

print("Sommets :")
print(g.nodes())
print("Aretes : ")
print(g.edges())