from CertifyingAlgo.SATChecker import resolveSAT, resolveUNSAT
from CertifyingAlgo.hamilton import hamiltontoClause

print("Est ce que mon assignation de variable est solution du problème du cycle Hamiltonien?")

print("Le sommet 1 a la position dans le cycle 5 attribuée")
print("Le sommet 2 a la position dans le cycle 4 attribuée")
print("Le sommet 3 a la position dans le cycle 1 attribuée")
print("Le sommet 4 a la position dans le cycle 2 attribuée")
print("Le sommet 5 a la position dans le cycle 3 attribuée")


# nombre de sommets
vertex = 5

# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon) (0 sur la diagonale un sommet A est considéré non connecté à lui même pour simplifier le code)
# Note : comparé à l'exemple du cours, l'arête entre A et E à été retiré pour rendre le problème UNSAT
edge = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

clauses = hamiltontoClause(edge, vertex)

print(clauses)
nameProof = "dratProof_test"

if resolveUNSAT(clauses, nameProof):
    print("L'assignation de variable est solution du problème")
else:
    print("L'assignation de variable n'est pas solution du problème")
