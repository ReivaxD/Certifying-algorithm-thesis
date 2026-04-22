from SAT.SATChecker import resolveSAT, resolveUNSAT
from SAT.hamilton import hamiltontoClause

print("Est ce que mon assignation de variable est solution du problème du cycle Hamiltonien?")

print("Le sommet 1 a la position dans le cycle 5 attribuée")
print("Le sommet 2 a la position dans le cycle 4 attribuée")
print("Le sommet 3 a la position dans le cycle 1 attribuée")
print("Le sommet 4 a la position dans le cycle 2 attribuée")
print("Le sommet 5 a la position dans le cycle 3 attribuée")


# nombre de sommets
vertex = 5

# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon) (0 sur la diagonale un sommet A est considéré non connecté à lui même pour simplifier le code)
edge = [[1, 1, 1, 0, 1], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 0, 1, 1, 1]]

clauses = hamiltontoClause(edge, vertex)

model = {1: False, 2: False, 3: False, 4: False, 5: True, # Le sommet 1 a la position dans le cycle 5 attribuée
        6: False, 7: False, 8: False, 9: True, 10: False, # Le sommet 2 a la position dans le cycle 4 attribuée
        11: True, 12: False, 13: False, 14: False, 15: False, # Le sommet 3 a la position dans le cycle 1 attribuée
        16: False, 17: True, 18: False, 19: False, 20: False, # Le sommet 4 a la position dans le cycle 2 attribuée
        21: False, 22: False, 23: True, 24: False, 25: False} # Le sommet 5 a la position dans le cycle 3 attribuée

if resolveSAT(clauses, model):
    print("L'assignation de variable est solution du problème")
else:
    print("L'assignation de variable n'est pas solution du problème")

# resolveUNSAT(clauses, model)