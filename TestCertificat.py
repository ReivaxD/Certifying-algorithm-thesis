import networkx as nx
import time
from CertifyingAlgo.CDCLSolver import CDCLSolver
from CertifyingAlgo.NkColor import colorNktoClause
from CertifyingAlgo.hamilton import hamiltontoClause
from CertifyingAlgo.NClique import cliqueNtoClause
from CertifyingAlgo.SATChecker import resolveSAT, resolveUNSAT

def toEdges(vertex, edges):
    tab = [[0 for _ in range(vertex)] for _ in range(vertex)]
    for tuple in edges:
        tab[tuple[0]][tuple[1]] = 1
        tab[tuple[1]][tuple[0]] = 1
    return tab

countSAT = 0
countUNSAT = 0
countSATVerified = 0
countSATUnverified = 0
countVerified = 0
countUnverified = 0

N = 4
name = "graph8.g6.txt"
with open("ressources/" + name, "r", encoding="utf-8") as f:
    nb_lignes = sum(1 for _ in f)

count = 0
cdcl_time = 0.0
cert_time = 0.0

start = time.time()

with open("ressources/" + name, "r", encoding="utf-8") as f:
    for ligne in f:
        g = nx.from_graph6_bytes(ligne.strip().encode())
        vertex = g.number_of_nodes()
        edge = toEdges(vertex, g.edges())

        clause = cliqueNtoClause(edge, vertex, N)

        t0 = time.time()
        solver = CDCLSolver(clause)
        sat = solver.solve()
        cdcl_time += time.time() - t0

        if sat[0]:
            countSAT += 1
            model = sat[1]

            t1 = time.time()
            ok = resolveSAT(clause, model)
            cert_time += time.time() - t1

            if ok:
                countSATVerified += 1
            else:
                countSATUnverified += 1
        else:
            countUNSAT += 1

            t1 = time.time()
            verified = resolveUNSAT(clause, name + "_" + str(count))
            cert_time += time.time() - t1

            if verified:
                countVerified += 1
            else:
                countUnverified += 1

        count += 1
        if nb_lignes > 1000 and (count % (nb_lignes // 10) == 0):
            print(str(count) + "/" + str(nb_lignes))

end = time.time()

print("Nombre de probleme SAT : " + str(countSAT))
print("  dont modeles verifies    : " + str(countSATVerified))
print("  dont modeles NON verifies: " + str(countSATUnverified))
print("Nombre de probleme UNSAT : " + str(countUNSAT))
print("  dont preuves vérifiées   : " + str(countVerified))
print("  dont preuves NON vérifiées : " + str(countUnverified))
print("Temps total :" + str(end - start) + "secondes")
print("  dont temps CDCL         : " + str(cdcl_time) + "secondes")
print("  dont temps certification: " + str(cert_time) + "secondes")
print("  dont temps overhead (I/O, boucle, etc.) : " + str((end - start) - cdcl_time - cert_time) + "secondes")