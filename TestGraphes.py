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


countSAT = 0
countUNSAT = 0
N = 3
name = "ressources/graph9.g6.txt"
with open(name, "r", encoding="utf-8") as f:
    nb_lignes = sum(1 for _ in f)

count = 0

with open(name, "r", encoding="utf-8") as f:
    for ligne in f:
        # 1044 graphes

        g = nx.from_graph6_bytes(ligne.strip().encode())
        vertex = g.number_of_nodes()
        edge = toEdges(vertex, g.edges())

        clause = colorNktoClause(edge, vertex, N)
        solver = CDCLSolver(clause)
        sat, model = solver.solve()

        if(sat):
            countSAT += 1
        else:
            countUNSAT += 1

        count += 1
        if count % (nb_lignes // 10) == 0:
            print(str(count) + "/" + str(nb_lignes))


print("Nombre de probleme SAT : " + str(countSAT))
print("Nombre de probleme UNSAT : " + str(countUNSAT))

