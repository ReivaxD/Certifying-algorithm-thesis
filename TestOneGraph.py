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

# Le code Graph6 du graphe souhaité
code = "FCXmW"

g = nx.from_graph6_bytes(code.encode())

print(g.nodes(), g.edges())

vertex = g.number_of_nodes()
edge = toEdges(vertex, g.edges())

# Le N-paramètre pour NkColor ou NClique
N = 3

clause = colorNktoClause(edge, vertex, N)
print(clause)
solver = CDCLSolver(clause)
sat, model = solver.solve()


if(sat):
    print(" Le probleme est resolvable" )
    print("Assignation possible :", model)

    print("Signification :")

    i = 1
    for x in range(vertex):
        for y in range(N):
            if(model[i] == True):
                print("Le sommet " + str(x+1) + " a la position dans la clique " + str(y+1) + " attribuee")
            i += 1
else:
    print(" Le probleme n'est pas resolvable" )