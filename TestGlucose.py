import networkx as nx
import time
from CertifyingAlgo.NkColor import colorNktoClause
from CertifyingAlgo.hamilton import hamiltontoClause
from CertifyingAlgo.NClique import cliqueNtoClause
from pysat.solvers import Glucose3

# Donne le format utilisé par les différents codes pour les arêtes
def toEdges(vertex, edges):
    tab = [[0 for _ in range(vertex)] for _ in range(vertex)]
    for tuple in edges:
        tab[tuple[0]][tuple[1]] = 1
        tab[tuple[1]][tuple[0]] = 1
    return tab

countSAT = 0
countUNSAT = 0


# Le N-paramètre pour NkColor ou NClique
N = 2
# Le nom du fichier dans le dossier ressources
name = "graph7.g6.txt"
with open("ressources/" + name, "r", encoding="utf-8") as f:
    nb_lignes = sum(1 for _ in f)

count = 0

start = time.time()

with open("ressources/" + name, "r", encoding="utf-8") as f:
    for ligne in f:

        g = nx.from_graph6_bytes(ligne.strip().encode())
        vertex = g.number_of_nodes()
        edge = toEdges(vertex, g.edges())

        clause = colorNktoClause(edge, vertex, N)

        solver = Glucose3()
        for c in clause:
            solver.add_clause(c)
        sat = solver.solve()
        if(sat):
            countSAT += 1
        else:
            countUNSAT += 1

        count += 1
        if nb_lignes > 1000 and (count % (nb_lignes // 10) == 0):
            print(str(count) + "/" + str(nb_lignes))

end = time.time()

print("Nombre de probleme SAT : " + str(countSAT))
print("Nombre de probleme UNSAT : " + str(countUNSAT))

print("Temps d'exécution :" + str(end - start) + "secondes")