from CertifyingAlgo.SATChecker import resolveSAT, resolveUNSAT
from CertifyingAlgo.hamilton import hamiltontoClause

print("Est ce qu'il existe une assignation de variable solution du problème du cycle Hamiltonien?")

# nombre de sommets
vertex = 5

# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon) (0 sur la diagonale un sommet A est considéré non connecté à lui même pour simplifier le code)
# Note : comparé à l'exemple du cours, l'arête entre A et E à été retiré pour rendre le problème UNSAT
edge = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

clauses = hamiltontoClause(edge, vertex)

print(clauses)
nameProof = "dratProof_test"

if resolveUNSAT(clauses, nameProof):
    print("L'assignation de variable est solution du probleme")
else:
    print("L'assignation de variable n'est pas solution du probleme")
