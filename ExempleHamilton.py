from SAT.CDCLSolver import CDCLSolver
from SAT.hamilton import hamiltontoClause

# nombre de sommets
vertex = 5

# un tableau R x R contenant un 1 si deux sommets sont connectés (0 sinon) (0 sur la diagonale un sommet A est considéré non connecté à lui même pour simplifier le code)
edge = [[1, 1, 1, 0, 1], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 0, 1, 1, 1]]

clause = hamiltontoClause(edge, vertex)

solver = CDCLSolver(clause)
sat, model = solver.solve()

if(sat):
    print(" Le problème est résolvable" )
else:
    print(" Le problème n'est pas résolvable" )

print("Assignation possible :", model)

print("Signification :")

i = 1
for x in range(vertex):
    for y in range(vertex):
        if(model[i] == True):
            print("Le sommet " + str(x+1) + " a la position dans la clique " + str(y+1) + " attribuée")
        i += 1